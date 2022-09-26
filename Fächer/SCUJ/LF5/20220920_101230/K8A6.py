## +-------------------------------------+
## |         Schumacher-Variante         |
## +-------------------------------------+

def switch_ssp(parameter):
    return {
        "schere": "schere schneidet papier",
        "stein": "stein zertruemmert schere",
        "papier": "papier bedeckt stein"
    }.get(parameter,"weder schere, noch stein, noch papier")
print(switch_ssp(input("schere,stein,papier: ")))

## +-------------------------------------+
## |          Logische Variante          |
## +-------------------------------------+

s = input('Schere, Stein, Papier: ').lower()
if s == 'schere':
    print('Schere schneidet Papier.')
elif s == 'stein':
    print('Stein zertrümmert Schere.')
elif s == 'papier':
    print('Papier bedeckt Stein.')
else:
    print('Weder Schere, Stein noch Papier.')
