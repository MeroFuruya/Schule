# import random
# Karten = list(range(1, 100))
# random.shuffle(Karten)

ASS = 0
Karten = [ASS, 4, 2, 3]

def sort_cards(cards: list) -> None:
    for i in range(0, len(cards)):
        for j in range(i, len(cards)):
            if cards[i] > cards[j]:
                cards[i], cards[j] = cards[j], cards[i]
print(Karten)
sort_cards(Karten)
print(Karten)

