from time import sleep

class FiboPrime:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.fiboPrime = []

    def calculate(self, n):
        while (True):
            buf = self.x + self.y
            complexDiv = 0
            for number in range(1, buf+1):
                if buf % number == 0:
                    complexDiv += 1

            if complexDiv == 2:
                yield buf
                self.fiboPrime.append(buf)

            if len(self.fiboPrime) == n:
                return self.fiboPrime

            self.x = self.y
            self.y = buf

n = 11
for id, number in zip(range(n), FiboPrime().calculate(n)):
    print(f"number[{id+1}]: {number}")

