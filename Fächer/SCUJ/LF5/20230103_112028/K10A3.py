ASS = 0

Karten = [ASS, 4, 2, 3]

# selection sort, out of place
def sort_cards(cards: list) -> list:
    def get_min_index(cards: list) -> int:
        min_index = 0
        for i in range(1, len(cards)):
            if cards[i] < cards[min_index]:
                min_index = i
        return min_index
    r = []
    for _ in range(0, len(cards)):
        r.append(cards.pop(get_min_index(cards)))
    return r
        
print(sort_cards(Karten))

