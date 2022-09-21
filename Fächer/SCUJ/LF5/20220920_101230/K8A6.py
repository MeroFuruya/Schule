s = input('Schere, Stein, Papier: ').lower()
if s == 'schere':
    print('Schere schneidet Papier.')
elif s == 'stein':
    print('Stein zertrümmert Schere.')
elif s == 'papier':
    print('Papier bedeckt Stein.')
else:
    print('Weder Schere, Stein noch Papier.')
