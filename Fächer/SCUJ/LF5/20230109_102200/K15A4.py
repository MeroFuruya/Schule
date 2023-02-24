class Haus:
    def __init__(self, Straße: str, Hausnummer: str, Farbe: str, Preis: float, Stockwerkzahl: int, Quadratmeter: int):
        self.straße: str = Straße
        self.hausnummer: str = Hausnummer
        self.farbe: str = Farbe
        self.preis: float = Preis
        self.stockwerkzahl: int = Stockwerkzahl
        self.quadratmeter: int = Quadratmeter

    def print_haus(self) -> None:
        print(""
            + f"Straße:        {self.straße}\n"
            + f"Hausnummer:    {self.hausnummer}\n"
            + f"Farbe:         {self.farbe}\n"
            + f"Preis:         {self.preis}\n"
            + f"Stockwerkzahl: {self.stockwerkzahl}\n"
            + f"Quadratmeter:  {self.quadratmeter}"
        )
    def neuer_anstrich(self, farbe: str):
        self.farbe = farbe


h = Haus("astrasse", "aHausnummer", "afarbe", 169.96, 88, 420)
h.neuer_anstrich("neonorange")
print(h.farbe)

