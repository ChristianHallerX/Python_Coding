# What is left shifting and right shifting a number?

A=13
print("decimal number thirteen:", A)
print("binary number thirteen: {0:b}\n".format(A))

print("Shift by n=2\n")

print("Left shift = add n zeros to the end, remove n bits on the front if they are non-zero")
print("Left-shifted binary: {0:b}".format(A<<2))
print("Left-shifted decimal:",A<<2,"\n")

print("Right shift: remove n bits from the end, add n copies of first bit to the front")
print("right-shifted binary: {0:b}".format(A>>2))
print("Right-shifted decimal:",A>>2)
