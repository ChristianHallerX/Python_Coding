'''
371. Sum of Two Integers (medium)

Given two integers a and b, return the sum of the two integers without using the operators + and -.
'''

# O(1) constant time complexity
def getSum(a: int, b: int) -> int:
    '''First XOR (Exclusive Or, ^), then AND with bitshift by 1, do this repeatedly in loop'''

    mask = 0xffffffff  # python workaround: hex of 32bit mask, since python uses arbitrarily large binaryies

    # loop until carry value b is 0 -> no more carry
    while b != 0:
        tmp_a = a
        a = (a ^ b) & mask  # ^ = XOR binary operation, mask = python workaround
        b = ((tmp_a & b) <<1) & mask # carry: & = AND binary operation, then bithshift 1 <<, mask = python workaround

    if a > mask // 2:  # python workaround
        return ~(a ^ mask)
    else:
        return a


def main():
    print(getSum(a=1, b=2), 'expected: 3')
    print(getSum(a=2, b=3), 'expected: 5')


if __name__ == '__main__':
    main()
