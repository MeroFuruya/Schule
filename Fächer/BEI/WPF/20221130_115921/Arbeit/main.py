def aufgabe4():
    ### ORIGINAL: ###
    # lerngruppe = ("Burak", "Marcel", "Tekiet", "Philip")
    # sort(lerngruppe)
    # lerngruppe.append("Dimitri", "Wladimir")
    # neueSchueler ["Angela", "Joe", "Donald"]
    # lerngruppe.extend("neueSchueler")
    # lerngruppe.remove["Dimitri"]
    # print("In der Klasse sind nun", lerngruppe.len, "Schüler.")
    # print("Der erste Schüler in der Liste ist", lerngruppe[1])

    # lerngruppe = ("Burak", "Marcel", "Tekiet", "Philip")
    ##### Wir wollen eine LISTE haben, nicht ein TUPLE! #####
    lerngruppe = ["Burak", "Marcel", "Tekiet", "Philip"]
    # sort(lerngruppe)
    ##### sort() ist eine Funktion, die nur auf Listen anwendbar ist! Jedoch gibt es eine funktion namens "sorted", die eine sortierte Kopie der liste zurückgibt, mit der wir dann die original liste überschreiben können #####
    lerngruppe.sort()  # oder lerngruppe = sorted(lerngruppe)
    # lerngruppe.append("Dimitri", "Wladimir")
    ##### append() nimmt nur ein Argument, also müssen wir die neuen Schüler in einer Liste zusammenfassen und mit der Listenfunktion "extend" oder durch addition der Schüleriste anfügen #####
    lerngruppe.extend(["Dimitri", "Wladimir"])  # oder lerngruppe += ["Dimitri", "Wladimir"]
    # neueSchueler ["Angela", "Joe", "Donald"]
    ##### Um eine variable zu definieren/manipulieren müssen wir ein Gleichzeichen setzen. #####
    neueSchueler = ["Angela", "Joe", "Donald"]
    # lerngruppe.extend("neueSchueler")
    ##### Um eine Variable zu referencen müssen wir ihren Namen nennen, also einfach nur blank text schreiben, ohne Anführungszeichen o.ä. #####
    lerngruppe.extend(neueSchueler)  # oder lerngruppe += neueSchueler
    # lerngruppe.remove["Dimitri"]
    ##### Um eine Funktion aufzurufen, müssen wir die Funktion mit "()" Klammern aufrufen. Eckige Klammern "[]" machen an der Stelle keinen Sinnn #####
    lerngruppe.remove("Dimitri")
    # print("In der Klasse sind nun", lerngruppe.len, "Schüler.")
    ##### Listen haben keine funktion/property/variable "len", sondern nur eine funktion namens "__len__()" #####
    ##### Des weiteren gibt es die Systemfunktion "len()", die auf Listen anwendbar ist. Diese funktion ruft jedoch auch nur die "__len__()" funktion auf und gibt ihren rückgabewert zurück ##### 
    print("In der Klasse sind nun", len(lerngruppe), "Schüler.")  # oder print(f"In der Klasse sind nun", lerngruppe.__len__(), "Schüler.")
    # print("Der erste Schüler in der Liste ist", lerngruppe[1])
    ##### Listen sind 0-indexiert, also ist der erste Eintrag in der Liste der Eintrag mit dem Index 0 #####
    print("Der erste Schüler in der Liste ist", lerngruppe[0])

def aufgabe5():
    # Schreiben Sie ein Programm, welches folgende Funktionalität umsetzt:
    # Der Benutzer wird zu Beginn aufgefordert, zwei ganze Zahlen a und b einzugeben.
    # Anschließend berechnet das Programm die Summe aller ganzen Zahlen von a bis b und gibt diese auf der Konsole aus.
    def inputInt(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Bitte geben Sie eine ganze Zahl ein!")
    a = inputInt("Bitte geben Sie Zahl \"a\" ein: ")
    b = inputInt("Bitte geben Sie Zahl \"b\" ein: ")
    
    n = 0;
    for i in range(a, b+1):
        n += i
    print(f"Die Summe aller ganzen Zahlen von {a} bis {b} ist {n}.")
    

def aufgabe6():
    ### Gegeben ist folgender Codeausschnitt (gehen Sie davon aus, dass "zahlenliste" eine vorher definierte Liste bestehend aus Zahlen ist).
    ### Leider hat der Entwickler keine Kommentare verwendet und auch die von ihm gewählten Variablennamen sind "nicht besonders aussagekräftig":
    # omg = 0
    # lol = 0
    # rofl = zahlenliste[0]
    # for wtf in zahlenliste:
    #     if wtf < rofl:
    #         rofl = wtf
    #         omg = lol
    #     lol = lol + 1
    # print(omg)
    
    # zahlenliste ist hier für debugging purposes erstellt
    import random
    random.seed()
    zahlenliste = random.sample(range(1, 100), 10)
    
    # last iteration - and index - where "wtf < rofl" was true
    ### omg -> indexOfSmallest
    
    indexOfSmallest = 0
    # counter - counts the number of iterations
    ### lol -> i
    i = 0
    # currently smallest number
    ### rofl -> smallestNumber
    smallestNumber = zahlenliste[0]
    # n/wtf: current number
    ### wtf -> n
    for n in zahlenliste:
        if n < smallestNumber:
            smallestNumber = n
            indexOfSmallest = i
        i = i + 1
    print(f"Index der kleinsten Zahl: {indexOfSmallest}")
    
def aufgabe7():
    # Schreiben Sie einen Codeabschnitt (wenn Sie möchten in Form einer Funktion "ZeigeAlleMatchups(spielerzahl)", das ist aber keine Pflicht),
    # welcher (wie im obigen Beispiel) alle möglichen Spielkonstellationen ausgibt - abhängig von einer vom Benutzer auf der Konsole eingegebenen Spielerzahl.
    # S1 bis S5
    
    teams = ["S1", "S2", "S3", "S4", "S5"]
    
    aufstellungen = []
    
    for team in teams:
        for team2 in teams:
            if team != team2 and not (team2, team) in aufstellungen:
                aufstellungen.append((team, team2))
    for aufstellung in aufstellungen:
        print(" gegen ".join(aufstellung))
    
