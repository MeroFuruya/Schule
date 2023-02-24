class Haus:
    def __init__(self, Straße: str, Hausnummer: str, Farbe: str, Preis: float, Stockwerkzahl: int, Quadratmeter: int):
        self.straße: str = Straße
        self.hausnummer: str = Hausnummer
        self.farbe: str = Farbe
        self.preis: float = Preis
        self.stockwerkzahl: int = Stockwerkzahl
        self.quadratmeter: int = Quadratmeter


h = Haus("astrasse", "bHausnummer", "cfarbe", 169.96, 88, 420)

print(""
        + f"Straße:        {h.straße}\n"
        + f"Hausnummer:    {h.hausnummer}\n"
        + f"Farbe:         {h.farbe}\n"
        + f"Preis:         {h.preis}\n"
        + f"Stockwerkzahl: {h.stockwerkzahl}\n"
        + f"Quadratmeter:  {h.quadratmeter}"
)

