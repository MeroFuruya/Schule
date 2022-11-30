### Standart Datentypen
# Integer (Ganzzahl) - 1, 2, -2134, 0
# Float (Fließkommazahl) - 1.0, 2.5, -2134.123, 0.0
# String (Zeichenkette) - "Hallo", "Welt", "1234", "1.0"
# Boolean (Wahrheitswert) - True, False

### Komplexe, zusammengesetzte Datentypen, Klassen, Objektdatentypen
# Tuple (Tupel) - () - unveränderlich
# List (Liste) - [] - veränderlich
# Dictionary, Hashtable (Wörterbuch, hash-tabelle) - {"" : ""}
# HashSet (Menge) - set()

# anlegen einer Liste
nameArray = ["Lars", "Peter", "Hans", "Klaus"]


# ausgebe des Listeninhalts
print(nameArray)

# Zugriff auf das erste Element
print(nameArray[0])

# Veränderung des zweiten Elements
nameArray[1] = "Karl"

# Ausgabe des Listeninhalts
print(nameArray)

# Es gibt viele weitere Listenfunktionen/-methoden, die uns bei der arbeit mit Listen helfen


def unpack(arr: list) -> list:
    result = []
    for elem in arr:
        if isinstance(elem, list):
            result.extend(unpack(elem))
        else:
            result.append(elem)
    return result

print(unpack(["a", ["b", "c"], "d", ["e", ["f", ["g"], "h"], "i", "j"], "k", "l"]))

schueler = ["max"]

# some other code
print(schueler)
for schueler in ["lamo"]:
    print(schueler)

print(schueler)

def test():
    print("hello")
    print(test.hello)
    test.a = "ur mom"

test.hello = "world"

test.laugth = "haha"

print(test.laugth)

test()

print(test.a)
