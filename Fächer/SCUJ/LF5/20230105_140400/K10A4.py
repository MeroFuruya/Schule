ASS = 0

karten = [ASS, 4, 2, 3]

import random

karten = list(range(1000000))
random.shuffle(karten)


# selection sort, in place

def sort_cards(cards: list) -> None:
    def get_min_index(start_index: int) -> int:
        r = start_index
        for i in range(start_index+1, len(cards)):
            if cards[i] < cards[r]:
                r = i
        return r
    for i in range(1, len(cards)):
        cards.insert(i, cards.pop(get_min_index(i)))

print(karten)
sort_cards(karten)
print(karten)

