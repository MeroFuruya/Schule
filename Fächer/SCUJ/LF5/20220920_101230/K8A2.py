ilist = []
i = ''
while type(i) is not int:
    try:
        i = int(input('Zahl1: '))
        ilist.append(i)
    except ValueError:
        print('Bitte eine Zahl eingeben!')

i = ''
while type(i) is not int:
    try:
        i = int(input('Zahl2: '))
        ilist.append(i)
    except ValueError:
        print('Bitte eine Zahl eingeben!')

i = ''
while type(i) is not int:
    try:
        i = int(input('Zahl3: '))
        ilist.append(i)
    except ValueError:
        print('Bitte eine Zahl eingeben!')

# ilist in aufsteigender Reihenfolge sortieren
ilist.sort()

# ilist in string-liste umwandeln
slist = []
for i in ilist:
    slist.append(str(i))

print(f'Aufsteigend Sorierte Liste: {",".join(slist)}')