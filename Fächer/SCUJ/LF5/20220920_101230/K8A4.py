print('HANDYKAUF')
# preis < 1000
preis = ''
while type(preis) is not float:
    try:
        preis = float(input('Preis: '))
    except ValueError:
        print('Bitte eine Zahl eingeben!')

# rückkammeras >= 3
rückkamera = ''
while type(rückkamera) is not int:
    try:
        rückkamera = int(input('Rückkamera: '))
    except ValueError:
        print('Bitte eine Zahl eingeben!')

# tage_ohne_laden >= 2
tage_ohne_laden = ''
while type(tage_ohne_laden) is not int:
    try:
        tage_ohne_laden = int(input('Tage ohne laden: '))
    except ValueError:
        print('Bitte eine Zahl eingeben!')

# marke.lower() in ['apple', 'samsung']
marke = input('Marke: ').lower()

answerlist = []
if preis >= 1000:
    answerlist.append('der preis zu hoch ist')
if rückkamera < 3:
    answerlist.append('es zu wenige Rückkameras hat')
if tage_ohne_laden < 2:
    answerlist.append('es nur weniger als 2 Tage ohne laden durchhält')
if marke not in ['apple', 'samsung']:
    answerlist.append('es nicht von der Marke Apple oder Samsung stammt')

if len(answerlist) == 0:
    print('Handy wird gekauft.')
else:
    print(f'Handy wird nicht gekauft, da {" und ".join(answerlist)}.')

