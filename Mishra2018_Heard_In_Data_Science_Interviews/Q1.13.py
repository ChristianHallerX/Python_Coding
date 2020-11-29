# How can you quickly determine if a number is a power of 2?

print("Every power of 2 has exactly 1 bit set to 1 (the bit in that number's log base-2 index).\n \
      So when subtracting 1 from it, that bit flips to 0 and all preceding bits flip to 1.\n \
      That makes these 2 numbers the inverse of each other so when AND-ing them, we will get 0 as the result.")

n = 4
print("n = {}".format(n))
print((n & (n-1) == 0))
