from random import randrange
# import random

class Funnydice:

    def __init__(self, n=6):
        self.n = n
        self.number = list(range(1, n + 1))
        self.index = randrange(0, self.n)
        self.val = self.number[self.index]

    def throw(self):
        self.index = randrange(0, self.n)
        self.val = self.number[self.index]

    def getval(self):
        return self.val


def get_input():
    inp = int(input('Enter a number: '))
    return inp


def main():
    n = get_input()
    obj = Funnydice(n)
    obj.throw()
    print(f"{n}면체 주사위 던지기의 임의의 숫자는 {obj.getval}")
    print(__name__)
    # print(random.__name__)


if __name__ == '__main__':
    main()