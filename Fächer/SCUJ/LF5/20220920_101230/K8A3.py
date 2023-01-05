preis = float(input('Preis: '))
klimaanlage = input('Klimaanlage (j/n): ').lower()


if preis < 20000 and klimaanlage == 'j':
    print('Auto wird gekauft.')
elif preis < 20000 and klimaanlage == 'n':
    print('Auto wird nicht gekauft, da es keine klimaanlage hat.')
elif preis >= 20000 and klimaanlage == 'j':
    print('Auto wird nicht gekauft, da es zu teuer ist.')
elif preis >= 20000 and klimaanlage == 'n':
    print('Auto wird nicht gekauft, da es zu teuer ist und keine klimaanlage hat.')
