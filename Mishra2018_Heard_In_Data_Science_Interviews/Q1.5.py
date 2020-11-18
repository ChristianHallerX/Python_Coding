# Given a positive number n, efficiently generate all binary numbers between 1 and n.

def bingen(n):
    for i in range(1, n+1):
        print('{0:b}'.format(i))


bingen(10)
