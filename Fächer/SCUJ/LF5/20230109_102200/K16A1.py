class Haus:
    def __init__(self, Straße: str, Hausnummer: str, Farbe: str, Preis: float, Stockwerkzahl: int, Quadratmeter: int):
        self.straße: str = Straße
        self.hausnummer: str = Hausnummer
        self.farbe: str = Farbe
        self.preis = Preis
        self.stockwerkzahl: int = Stockwerkzahl
        self.quadratmeter = Quadratmeter
       
    def print_haus(self) -> None:
        print(""
            + f"Straße:        {self.straße}\n"
            + f"Hausnummer:    {self.hausnummer}\n"
            + f"Farbe:         {self.farbe}\n"
            + f"Preis:         {self.preis}\n"
            + f"Stockwerkzahl: {self.stockwerkzahl}\n"
            + f"Quadratmeter:  {self.quadratmeter}"
        )
    
    @property
    def preis(self) -> float:
        return self._preis
    
    @preis.setter
    def preis(self, val) -> None:
        if val >= 0:
            self._preis = val

    @property
    def quadratmeter(self) -> int:
        return self._quadratmeter
    
    @quadratmeter.setter
    def quadratmeter(self, val) -> None:
        if val >= 0:
            self._quadratmeter = val

hausliste: list[Haus] = [
    Haus("astrasse", "aHausnummer", "afarbe", 169.96, 88, 420),
    Haus("bstrasse", "bHausnummer", "bfarbe", 169.97, 1080, 720),
    Haus("cstrasse", "cHausnummer", "cfarbe", 143, 1234, 3),
]

for h in hausliste:
    if h.preis > 200.000:
        hausliste.remove(h)

for h in hausliste:
    h.print_haus()

