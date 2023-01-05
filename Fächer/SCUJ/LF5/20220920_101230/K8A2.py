ilist = []
i = int(input("Zahl1: "))
ilist.append(i)

i = int(input("Zahl2: "))
ilist.append(i)

i = int(input("Zahl3: "))
ilist.append(i)


## +-------------------------------------+
## |          Einfache Variante          |
## +-------------------------------------+
## nachteil: nicht flexibel - die liste muss immer 3 elemente haben
## sonst gibt es einen indexerror
## wenn die liste mehr als 3 elemente hat, werden die letzten elemente ignoriert

# ilist in aufsteigender Reihenfolge sortieren
ilist.sort()
print("Aufsteigend Sorierte Liste:" + str(ilist[0]) + "," + str(ilist[1]) + "," + str(ilist[2]))


## +-------------------------------------+
## |          Flexible Variante          |
## +-------------------------------------+

# ilist in aufsteigender Reihenfolge sortieren
ilist.sort()
# ilist in string-liste umwandeln
slist = []
for i in ilist:
    slist.append(str(i))

print(f'Aufsteigend Sorierte Liste: {", ".join(slist)}')


## +-------------------------------------+
## |          EinzeilerVariante          |
## +-------------------------------------+

print(f'Aufsteigend Sorierte Liste: {", ".join([str(i) for i in sorted(ilist)])}')
