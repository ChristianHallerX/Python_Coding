# Q1.3 Write a program to roll a dice 1000 times and display how many times each number was rolled.

import random


def dieroller():
    mydict = {'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0, 'six': 0}
    random.seed(1)

    for i in range(1000):
        roll = random.randint(1, 6)
        if roll == 1:
            mydict['one'] += 1
        elif roll == 2:
            mydict['two'] += 1
        elif roll == 3:
            mydict['three'] += 1
        elif roll == 4:
            mydict['four'] += 1
        elif roll == 5:
            mydict['five'] += 1
        elif roll == 6:
            mydict['six'] += 1
    print(mydict)


dieroller()
