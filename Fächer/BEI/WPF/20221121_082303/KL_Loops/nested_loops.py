# Nested Loops
# Anwendungsbeispiele:
# - Zeichnen von Bildern
# - Berechnung von Flächen
# - Berechnung von Volumen
# - Iteration über zeridimensionale Listen

# Zweidimensionales arry erstellen

# Schulklasse <- Namen <- Noten

klassen = ["1a", "2a"]
namen = [["Max", "Bert", "Susanne"], ["Peter", "Klaus", "Hans"]]
noten = [[[1, 3, 5], [2, 4, 6], [3, 5, 7]], [[1, 3, 5], [2, 4, 6], [3, 5, 7]]]

# Ausgabe der Noten pro Schüler

for klasse in range(len(klassen)):
    print("Klasse: " + klassen[klasse])
    for schueler in range(len(namen[klasse])):
        print("  Schüler: " + namen[klasse][schueler])
        for note in range(len(noten[klasse][schueler])):
            print("    Note: " + str(noten[klasse][schueler][note]))
