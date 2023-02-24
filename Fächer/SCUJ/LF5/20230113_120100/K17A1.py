import random

random.seed()

class Fahrzeug:
    def __init__(self, ps: int, gewicht: float, verbrauch: float, max_geschwindigkeit: int, hubraum: float):
        self.ps: int = ps
        self.gewicht: float = gewicht
        self.verbrauch: float = verbrauch
        self.max_geschwindigkeit: int = max_geschwindigkeit
        self.hubraum: float = hubraum


class Auto(Fahrzeug):
    def __init__(self, ps: int, gewicht: float, verbrauch: float, max_geschwindigkeit: int, hubraum: float, tueren: int, radanzahl: int, anhaengerkupplung: bool):
        super().__init__(ps, gewicht, verbrauch, max_geschwindigkeit, hubraum)
        self.tueren: int = tueren
        self.radanzahl: int = radanzahl
        self.anhaengerkupplung: bool = anhaengerkupplung


class Motorrad(Fahrzeug):
    def __init__(self, ps: int, gewicht: float, verbrauch: float, max_geschwindigkeit: int, hubraum: float, beiwagen: bool):
        super().__init__(ps, gewicht, verbrauch, max_geschwindigkeit, hubraum)
        self.beiwagen: bool = beiwagen


v: list[Fahrzeug] = []

for i in range(3):
    v.append(Auto(
        ps=random.randint(20, 100),
        tueren=random.randint(2, 5),
        gewicht=random.randint(1000, 100000)/10,
        hubraum=random.randint(10, 50)/10,
        radanzahl=random.randint(3, 4),
        verbrauch=random.randint(10, 70)/10,
        anhaengerkupplung=bool(random.randint(0, 1)),
        max_geschwindigkeit=random.randint(30, 300)
        ))

for i in range(3):
    v.append(Motorrad(
        ps=random.randint(20, 100),
        gewicht=random.randint(1000, 100000)/10,
        hubraum=random.randint(10, 50)/10,
        verbrauch=random.randint(10, 70)/10,
        max_geschwindigkeit=random.randint(30, 300),
        beiwagen=bool(random.randint(0, 1))
        ))





