import random
random.seed()

class Dice:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    def roll(self):
        return random.randint(self.min, self.max)

class Attack:
    def __init__(self, name: str, dice: Dice, isPassive: bool = False, blocks: int = 1, on_execute = None):
        self.name: str = name
        self.isPassive = isPassive
        self.dice: Dice = dice
        self.blocks_for: int = blocks
        self.execution_count: int = 0
        self.customVars: dict(str, any) = {}
        self.on_execute: function(self, any, any) = on_execute
        
    def execute(self, target: any, executer: any):
        if self.on_execute != None:
            self.on_execute(self, target, executer)
        else:
            target.get_hit(self.dice.roll(), self)
        self.execution_count += 1

class Char:
    def __init__(self):
        self.name: str = ""
        self.initiative: Dice = None
        self.heal: Dice = None
        self.heal_used: bool = False
        self.lebenspunkte_dice: Dice = None 
        self.lebenspunkte: int = 0
        self.blocked_for: int = 0
        self.attacks: list(Attack) = []
        self.customVars: dict(str, any) = {}
        self.on_get_hit: function(self, Attack) = None
        self.on_next_round: function(self) = None
        self.on_do_hit: function(self, any, Attack) = None

    def next_round(self):
        if self.blocked_for > 0:
            self.blocked_for -= 1
        if self.on_next_round != None:
            self.on_next_round(self)
    
    def action_allowed(self) -> bool:
        return self.blocked_for == 0

    def get_hit(self, damage: int, attack: Attack):
        if self.on_get_hit != None:
            self.lebenspunkte -= self.on_get_hit(self, attack)
        else:
            self.lebenspunkte -= attack.roll()

    def do_hit(self, target: any, attack: str or Attack):
        if self.action_allowed():
            if type(attack) == str:
                for a in self.attacks:
                    if a.name == attack:
                        attack_obj = a
            elif type(attack) == Attack:
                attack_obj = attack
            else:
                raise Exception("Invalid type for attack")
            attack_obj = attack
            if self.on_do_hit != None:
                self.on_do_hit(self, target, attack_obj)
            attack_obj.execute(target, self)
            self.blocked_for = attack_obj.blocks_for
    
    def use_healpotion(self):
        if not self.heal_used:
            self.lebenspunkte += self.heal
            if self.lebenspunkte > self.lebenspunkte_dice:
                self.lebenspunkte = self.lebenspunkte_dice

    def roll_initiative(self) -> int:
        return self.initiative.roll()


def create_krieger(name: str):
    def on_get_hit(self: Char, attack: Attack) -> int:
        if self.customVars["do_defend"]:
            self.customVars["do_defend"] = False
            return attack.dice.roll() - Dice(1, 4).roll()
        return attack.dice.roll()
    def on_execute_schwertblock(self: Attack, target: Char, executor: Char) -> int:
        if self.name == "Schwertblock":
            executor.customVars["do_defend"] = True
    krieger = Char()
    krieger.name = name
    krieger.initiatve = Dice(1, 8)
    krieger.lebenspunkte_dice = Dice(1, 10)
    krieger.lebenspunkte = krieger.lebenspunkte_dice.roll()
    krieger.heal = Dice(1, 6)
    krieger.customVars = {
        "do_defend": False
    }
    krieger.attacks = [
        Attack("Schwertschlag", Dice(1, 6)),
        Attack("Schwertblock", Dice(1, 4), True, 1, on_execute_schwertblock)
    ]
    krieger.on_get_hit = on_get_hit
    return krieger

def create_mage(name: str):
    def on_get_hit(self: Char, attack: Attack) -> int:
        if self.customVars["defend_for"]>0:
            self.customVars["defend_for"] -= 1
            if Dice(0, 1).roll() == 1:
                return 0
        return attack.dice.roll()
    def on_execute_spiegelbilder(self: Attack, target: Char, executor: Char):
        executor.customVars["defend_for"] = 2
    mage = Char()
    mage.name = name
    mage.initiatve = Dice(1, 6)
    mage.lebenspunkte_dice = Dice(1, 6)
    mage.lebenspunkte = mage.lebenspunkte_dice.roll()
    mage.heal = Dice(1, 6)
    mage.attacks = [
        Attack("Feuerball", Dice(2, 7), False, 2),
        Attack("Magic Missile", Dice(1, 4)),
        Attack("Spiegelbilder", Dice(0, 1), True, 1, on_execute_spiegelbilder)
    ]
    mage.on_get_hit = on_get_hit
    mage.customVars = {
        "defend_for": 0
    }
    return mage

def create_schurke(name: str):
    def on_do_hit(self: Char, target: Char, attack: Attack) -> int:
        if attack.name == "Dolchstich":
            self.customVars["dochstich_used"] += 1
            if self.customVars["dochstich_used"] > 2:
                for a in self.attacks:
                    if a.name == "Dolchstich":
                        self.attacks.remove(a)
        if attack.name == "Schmutz":
            def schmutz_on_do_hit(self: Char, target: Char, attack: Attack) -> int:
                self.attacks[attack.name] = Attack(attack.name, Dice(attack.dice.min, attack.dice.max), attack.blocks_for)
                attack.dice.min = 0
                attack.dice.max = 0
                self.on_do_hit = self.customVars["normal_on_do_hit"]
            if "normal_on_do_hit" not in target.customVars.keys():
                target.customVars["normal_on_do_hit"] = self.on_do_hit
            target.on_do_hit = schmutz_on_do_hit
    schurke = Char()
    schurke.name = name
    schurke.initiatve = Dice(1, 10)
    schurke.lebenspunkte_dice = Dice(1, 8)
    schurke.lebenspunkte = schurke.lebenspunkte_dice.roll()
    schurke.heal = Dice(1, 6)
    schurke.attacks = [
        Attack("Dolchstich", Dice(1, 6)),
        Attack("Schmutz", Dice(1, 4), True)
    ]
    schurke.customVars = {
        "dochstich_used": 0
    }
    schurke.on_do_hit = on_do_hit
    return schurke

def check_if_done(chars: list) -> bool:
    for char in chars:
        if char.lebenspunkte > 0:
            return False
    return True

chars = [create_krieger("krieger"), create_mage("mage"), create_schurke("schurke")]

while not check_if_done(chars):
    for char in chars:
        if char.lebenspunkte > 0:
            char.next_round()
            # print life point table
            print("| "+(" |\n| ".join([f"{char.name:10} | {char.lebenspunkte :3} | {}" for char in chars])+ " |"))
            
            print(f"{char.name} hat {char.lebenspunkte} Lebenspunkte und ist am Zug")
                    
            print("Attacks:")
            for i in range(len(char.attacks)):
                print(f"{i}: {char.attacks[i].name}")
            if not char.heal_used:
                print(f"{len(char.attacks)}: Heal")
            sel_attack_str = input("Welchen Angriff willst du ausführen? ")
            sel_attack = -1
            while sel_attack < 0 or sel_attack > len(char.attacks):
                try:
                    sel_attack = int(sel_attack_str)
                except:
                    sel_attack_str = input("Bitte gib eine Zahl ein: ")
            if not char.attacks[sel_attack].isPassive:
                for i in range(len(chars)):
                    if chars[i] != char:
                        print(f"{i}: {chars[i].name}")
                sel_target_str = input("Welchen Gegner willst du angreifen? ")
                sel_target = -1
                while sel_target < 0 or sel_target > len(chars) or chars[sel_target] == char:
                    try:
                        sel_target = int(sel_target_str)
                    except:
                        sel_target_str = input("Bitte gib eine Zahl ein! ")
            
            char.do_hit(chars[sel_target], char.attacks[sel_attack])
            
            print("\n")
            