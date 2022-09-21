def ende():
    inp = ''
    while inp != 0:
        inp = ''
        while type(inp) != int:
            try:
                inp = int(input('Zum Beenden 0 eingeben: '))
            except:
                print('Falsche Eingabe!')
                inp = ''
    print('Sie haben das Programm durch die eingabe von \'0\' beendet!')

ende()
