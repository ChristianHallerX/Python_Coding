"""
Given an integer n, return the smallest prime palindrome greater than or equal to n.

An integer is prime if it has exactly two divisors: 1 and itself. Note that 1 is not a prime number.

For example, 2, 3, 5, 7, 11, and 13 are all primes.
An integer is a palindrome if it reads the same from left to right as it does from right to left.

For example, 101 and 12321 are palindromes.

Example 1:

Input: n = 6
Output: 7
Example 2:

Input: n = 8
Output: 11
"""


def primepalindrome(n):
    if n < 0:
        print("n should be larger 0")
        return
    n += 1

    while True:
        counter = 0
        # find prime first
        for i in range(1, n + 1):
            if n % i == 0:
                counter += 1

        # is palindrome?
        if counter == 2:
            if str(n) == str(n)[::-1]:
                return n

        n += 1


"""
The solution involves:
(1) generating palindromes starting from a given number 'n' and
(2) checking if they are prime.

The algorithm generates palindromes by mirroring the first half of the number and checks for primality using
trial division. 

The process continues until a prime palindrome is found.

"""


def isPrime(number):

    # Check if the number is less than 2, which is not prime
    if number < 2:
        return False

    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def nextPalindrome(n):
    """
    Goal: Generate a palindrome that's larger than 'n'.
    - Take any number 'n' and generate a palindrome by mirroring the first half.
    - If the palindrome is valid (larger n), then return it.
    - Otherwise, increment the half, mirror, then return.
    """

    # Convert the number to a string
    strN = str(n)

    # Get the length of the number
    length = len(strN)

    # Generate the first half of the palindrome
    half = strN[: (length + 1) // 2]

    # Create the palindrome by mirroring the first half
    if length % 2 == 0:
        palindrome = int(half + half[::-1])
    else:
        palindrome = int(half + half[-2::-1])

    # If the palindrome is less than n, increment the half and regenerate
    if palindrome < n:
        half = str(int(half) + 1)
        if length % 2 == 0:
            palindrome = int(half + half[::-1])
        else:
            palindrome = int(half + half[-2::-1])

    return palindrome


def smallestPrimePalindrome(n):
    if n < 0:
        print("n should be larger 0")
        return
    # Start with the given number n
    candidate = n

    # Continue until a prime palindrome is found
    while True:

        # Generate the next palindrome
        candidate = nextPalindrome(candidate)

        # Check if the candidate is prime
        if isPrime(candidate):
            return candidate

        # Increment the candidate for the next iteration
        candidate += 1


if __name__ == "__main__":
    print(primepalindrome(6))
    print(primepalindrome(8))
    print(primepalindrome(99))
    print(primepalindrome(102))
    print(primepalindrome(-199))
    print(primepalindrome(200))

    print("\n")
    print(smallestPrimePalindrome(6))
    print(smallestPrimePalindrome(8))
    print(smallestPrimePalindrome(99))
    print(smallestPrimePalindrome(102))
    print(smallestPrimePalindrome(-199))
    print(smallestPrimePalindrome(200))
