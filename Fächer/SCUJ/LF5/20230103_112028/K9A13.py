class Rückgeld:
    def __init__(self, zwanzig: int, euro: int):
        self.zwanzig = zwanzig
        self.euro = euro

def wechselautomat(geld: int) -> Rückgeld:
    return Rückgeld(geld // 20, geld % 20)

Rückgeld = wechselautomat(55)
print(Rückgeld.zwanzig, Rückgeld.euro)
