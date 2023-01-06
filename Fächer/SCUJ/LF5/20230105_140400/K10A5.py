ASS = 0

karten = [ASS, 4, 2, 3]

karten = list(range(45))

karten.reverse()
# import random

# random.shuffle(karten)

count = 0

# bubblesort, in place

def sort_cards(cards: list) -> None:
    global count
    count += 1
    for i in range(0, len(cards)-1):
        if cards[i] > cards[i+1]:
            cards[i], cards[i+1] = cards[i+1], cards[i]
            # print(cards)
            sort_cards(cards)

print(karten)
sort_cards(karten)
print(karten)
print(count)

