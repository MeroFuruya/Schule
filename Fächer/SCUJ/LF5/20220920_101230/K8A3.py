preis = ''
while type(preis) is not float:
    try:
        preis = float(input('Preis: '))
    except ValueError:
        print('Bitte eine Zahl eingeben!')

klimaanlage = ''
while klimaanlage not in ['ja', 'nein', 'j', 'n', 'y']:
    try:
        klimaanlage = input('Klimaanlage (j/n): ').lower()
    except ValueError:
        print('Bitte j oder n eingeben!')

preisok = False

if preis < 20000 and klimaanlage in ['ja', 'j', 'y']:
    print('Auto wird gekauft.')
elif preis < 20000 and klimaanlage in ['nein', 'n']:
    print('Auto wird nicht gekauft, da es keine klimaanlage hat.')
elif preis >= 20000 and klimaanlage in ['ja', 'j', 'y']:
    print('Auto wird nicht gekauft, da es zu teuer ist.')
elif preis >= 20000 and klimaanlage in ['nein', 'n']:
    print('Auto wird nicht gekauft, da es zu teuer ist und keine klimaanlage hat.')
