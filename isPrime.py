def isPrime(num):
    if num > 1:                     # only check numbers larger 1
        for i in range(2,num):      # check for all values smaller than the number
            if (num % i) == 0:      # Primes always have modulus >0. If the modulus is zero, it cannot be prime
                answer = False
                break
        else:
            answer = True           # The case that the loop ran without finding a zero modulus
    else:
        answer = False              # The case that number 1 was entered, which is never prime
    return answer
   
# testing - prints all prime numbers - where function delivers True
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
