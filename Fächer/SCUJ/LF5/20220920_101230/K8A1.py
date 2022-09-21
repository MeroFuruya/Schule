i1 = ''
while type(i1) is not int:
    try:
        i1 = int(input('Zahl 1: '))
    except ValueError:
        print('Bitte eine Zahl eingeben!')

i2 = ''
while type(i2) is not int:
    try:
        i2 = int(input('Zahl 2: '))
    except ValueError:
        print('Bitte eine Zahl eingeben!')

# überprüfen, ob i1 kleiner ist als i2
if i1 < i2:
    print('i1 ist kleiner als i2')
elif i1 > i2:
    print('i1 ist größer als i2')
else:
    print('i1 ist gleich i2')
