# <codecell>Function definition

"""
Created on Wed Dec 28 17:22:13 2021

@author: Christian Haller
"""

def fizzBuzz(number):
    """Print all numbers below a given number. If a number div by 3,
    print 'fizz', if div by 5, then 'buzz', if 3 and 5 then 'fizzbuzz'.
    """
    for i in range(number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, 'fizzbuzz (div by 3 and 5)')
        elif i % 3 == 0:
            print('fizz (div by 3)')
        elif i % 5 == 0:
            print('buzz (div by 5)')
        else:
            print(i)


def fizzBuzz2(number):
    for i in range(number):
        # multiply boolean with string
        print(((i % 3 == 0) * 'fizz' + (i % 5 == 0) * 'buzz') or i)


def main():
    fizzBuzz(16)
    fizzBuzz2(16)

if __name__ == '__main__':
    main()
