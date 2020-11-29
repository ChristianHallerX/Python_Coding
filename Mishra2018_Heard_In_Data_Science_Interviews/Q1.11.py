# How would you write -5 in binary?

positive=5

print("Decimal:", positive)
print("Binary: {0:b}\n".format(positive))

negative=-5

print("Decimal:", negative)
print("Binary: {0:b}".format(negative))

print("Python actually adds a sign to the bits.\n Other languages also use signed bits, i.e. the first, most significant bit is used as sign 1=negative, 0=positive,\n leaving one bit less for the magnitude bits.")
