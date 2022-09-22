import random


class Guesser:
    def __init__(self):
        self.lastGuess = -1
        self.lastGuessTooHigh: bool = False
        self.guessCount = 0
        self.alreadyGuessed = {}

    def _doGuess(self, guess):
        self.guessCount += 1
        return guess
    
    def afterGuess(self, tooHigh: bool):
        self.lastGuessTooHigh = tooHigh
        self.alreadyGuessed[self.lastGuess] = tooHigh

    def rangeAlreadyGuessed(self, low, high):
        for i in range(low, high):
            if i in self.alreadyGuessed.keys():
                return True
        return False
    
    def nearestNumberAlreadyGuessed(self, n):
        nearestNumber = -1
        for i in self.alreadyGuessed.keys():
            if i < n and i > nearestNumber:
                nearestNumber = i
        return nearestNumber

    

    def Guess(self):
        # first guess
        if self.guessCount == 0:
            return self._doGuess(50)

        if self.lastGuessTooHigh:
            # if last guess was too high
            #   get last number that was too low
            #   go halfway between that number and the last guess
            nearestNumber = self.nearestNumberAlreadyGuessed(self.lastGuess)
            if nearestNumber == -1:
                return self._doGuess(0)
            else:
                return self._doGuess((self.lastGuess + nearestNumber) // 2)
        else:
            # last guess was too low
            #   get last number that was too high
            #   go halfway between that number and the last guess
            nearestNumber = self.nearestNumberAlreadyGuessed(self.lastGuess)
            if nearestNumber == -1:
                return self._doGuess(100)
            else:
                return self._doGuess((self.lastGuess + nearestNumber) // 2)

random.seed()
secret_number = random.randint(0, 100)

print("Cracking Number")
print("===============")

print(f"Secret Number: {secret_number}")
g = Guesser()

for i in range(5):
    guess = g.Guess()
    if guess == secret_number:
        print("Correct!")
        break
    elif guess > secret_number:
        g.afterGuess(True)
        print(f"Guessed {guess}; Too high")
    else:
        print(f"Guessed {guess}; Too low")
        g.afterGuess(False)
