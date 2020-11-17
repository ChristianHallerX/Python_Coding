# Q1.2 Write a function to compute Fibonacci numbers recursively. What is time complexity?


def fibo(n):
    """ A recursive function that calculates a single Fibonacci number. The if statement stops the recursion."""
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# define the range of Fibonacci numbers to print
nterms = 10
for i in range(nterms):
    print(fibo(i))
