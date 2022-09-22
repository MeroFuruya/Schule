import random
import guesser



random.seed()
secret_number = random.randint(0, 100)

print("Cracking Number")
print("===============")

print(f"Secret Number: {secret_number}")
g = guesser.Guesser()

guesser.Guess(g, secret_number)

print("Number of guesses: ", g.guessCount)

# 
# # tests:
# print("Tests:")
# print("======")
# print(f"GUESSED: {g.alreadyGuessed}")
# print(f"range already Guessed 1, 100 {g.rangeAlreadyGuessed(0, 100)}")
# print(f"range already Guessed 1, 100 {g.rangeAlreadyGuessed(0, 50)}")
# print(f"range already Guessed 1, 100 {g.rangeAlreadyGuessed(50, 100)}")
# print()
# print(f"closestNumberAlreadyGuessed 50: {g.closestNumberAlreadyGuessed(50)}")
# print(f"closestNumberAlreadyGuessed 75: {g.closestNumberAlreadyGuessed(75)}")
# print(f"closestNumberAlreadyGuessed 25: {g.closestNumberAlreadyGuessed(25)}")
# print(f"closestNumberAlreadyGuessed 0: {g.closestNumberAlreadyGuessed(0)}")
# print(f"closestNumberAlreadyGuessed 100: {g.closestNumberAlreadyGuessed(100)}")
# print()
# 