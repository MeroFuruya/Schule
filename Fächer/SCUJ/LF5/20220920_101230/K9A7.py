import random

random.seed()

# this is just for debug purposes :)
# print("CRACKING NUMBER")

secret_number = random.randint(1, 100)

print(secret_number)

for try_count in range(5):
    ui = ''
    while type(ui) != int:
        try:
            ui = int(input("Gib eine Zahl zwischen 0 und 100 ein: "))
        except:
            print("Invalid input!")
            ui = ''
    if ui < secret_number:
        print("Zu niedrig")
    elif ui > secret_number:
        print("Zu hoch")
    elif ui == secret_number:
        print("Richtig! Du hast gewonnen!")
        break

if ui != secret_number:
    print("Du hast verloren!")
    print(f"Die Zahl war: {secret_number}.")
