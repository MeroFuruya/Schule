class Guesser:
    def __init__(self, maxNumber=100, minNumber=0):
        self.lastGuess = -1
        self.lastGuessTooHigh: bool = False
        self.guessCount = 0
        self.alreadyGuessed = {}
        self.minNumber = minNumber
        self.maxNumber = maxNumber

    def _doGuess(self, guess):
        self.guessCount += 1
        self.lastGuess = guess
        return guess
    
    def afterGuess(self, tooHigh: bool):
        self.lastGuessTooHigh = tooHigh
        self.alreadyGuessed[self.lastGuess] = tooHigh

    def rangeAlreadyGuessed(self, low, high):
        for i in range(low, high):
            if i in self.alreadyGuessed.keys():
                return True
        return False
    
    def closestNumberAlreadyGuessed(self, n: int):
        arr = []
        for k, v in self.alreadyGuessed.items():
            if v != self.lastGuessTooHigh:
                arr.append(k)
        if len(arr) == 0:
            return -1
        curr = arr[0]
        for i in arr:
            if abs(n - i) < abs(n - curr):
                curr = i
        return curr


    def Guess(self):
        # first guess
        if self.guessCount == 0:
            return self._doGuess(int(self.maxNumber - self.minNumber // 2))
        else:
            if self.lastGuessTooHigh:
                # if last guess was too high
                #   get last number that was too low
                #   go halfway between that number and the last guess
                closestNumber = self.closestNumberAlreadyGuessed(self.lastGuess)
                if closestNumber == -1:
                    return self._doGuess(self.minNumber)
                else:
                    return self._doGuess((self.lastGuess + closestNumber) // 2)
            else:
                # last guess was too low
                #   get last number that was too high
                #   go halfway between that number and the last guess
                closestNumber = self.closestNumberAlreadyGuessed(self.lastGuess)
                if closestNumber == -1:
                    return self._doGuess(self.maxNumber)
                else:
                    return self._doGuess((self.lastGuess + closestNumber) // 2)


def Guess(g: Guesser, secret_number: int, doPrint: bool = True):
    while True:
        guess = g.Guess()
        if guess == secret_number:
            if doPrint: print("Correct!")
            return g.guessCount
        elif guess > secret_number:
            g.afterGuess(True)
            if doPrint: print(f"{g.guessCount}: Guessed {guess}; Too high")
        else:
            g.afterGuess(False)
            if doPrint: print(f"{g.guessCount}: Guessed {guess}; Too low")
