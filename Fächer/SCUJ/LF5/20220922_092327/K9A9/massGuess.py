import random
import guesser

random.seed()
print("Mass Guessing")
results = {}
neededTryes = []

max_num = 100
min_num = 1

for i in range(min_num, max_num):
#     print(i)
    secret_number = i
    g = guesser.Guesser(max_num, min_num)
    guesser.Guess(g, secret_number, False)
    results[secret_number] = g.guessCount
    neededTryes.append(g.guessCount)

print("Results:", results)

print("Max: ", max(neededTryes))
print("Min: ", min(neededTryes))
print("Avg: ", sum(neededTryes) / len(neededTryes))
