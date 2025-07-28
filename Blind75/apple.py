"""
This solution uses the Hash Set Lookup algorithm to efficiently find the number of pairs of integers
in an array where the difference between the two numbers is equal to a given integer k. The algorithm
leverages a hash set to store unique elements and checks for the existence of complement numbers
that satisfy the condition. This allows for constant time complexity lookups, making the solution
efficient for large arrays.

The algorithm works by iterating through each number in the array and checking if the complement
(number + k or number - k) exists in the hash set. If it does, it increments the pair count. Each
number is then added to the hash set for future lookups. The result is returned modulo 10^9 + 7.
"""


def solution(k, a):

    # Define modulo constant
    modulo = 10**9 + 7

    # Initialize set of unique elements
    elementSet = set()

    # Initialize result counter
    pairCount = 0

    # Iterate through each number in the array
    for number in a:

        # Check if the complement (number + k) exists in the set
        if (number + k) in elementSet:
            pairCount += 1

        # Check if the complement (number - k) exists in the set
        if (number - k) in elementSet:
            pairCount += 1

        # Add number to set
        elementSet.add(number)

    # Return pair count modulo
    return pairCount % modulo


if __name__ == "__main__":
    k = 59

    a = [
        262,
        262,
        683,
        41,
        848,
        723,
        324,
        272,
        122,
        154,
        335,
        821,
        457,
        365,
        747,
        171,
        776,
        269,
        218,
        701,
        703,
        653,
        933,
        907,
        959,
        728,
        806,
        797,
        720,
        84,
        308,
        334,
        698,
        991,
        376,
        898,
        715,
        52,
        171,
        189,
        559,
        506,
        10,
        16,
        224,
        109,
        539,
        0,
        378,
        109,
        53,
        81,
        114,
        338,
        989,
        426,
        67,
        147,
        223,
        787,
        231,
        532,
        122,
        281,
        875,
        850,
        179,
        590,
        254,
        350,
        131,
        813,
        857,
        494,
        181,
        81,
        603,
        720,
        433,
    ]
    print(solution(k, a))
    k = 43

    a = [
        39,
        2,
        428,
        403,
        500,
        681,
        647,
        538,
        159,
        151,
        535,
        134,
        339,
        632,
        215,
        127,
        504,
        629,
        49,
        964,
        285,
        429,
        343,
        335,
        177,
        900,
        238,
        571,
        949,
        289,
        367,
        988,
        292,
        795,
        743,
        144,
        829,
        390,
        682,
        340,
        541,
        569,
        826,
        232,
        261,
        42,
        360,
        117,
        23,
        761,
        81,
        309,
        190,
        425,
        996,
        367,
        677,
        234,
        690,
        626,
        524,
        57,
        614,
        168,
        205,
        358,
        312,
        386,
        100,
        346,
        726,
        994,
        916,
        552,
        578,
        529,
        946,
        290,
        647,
        970,
        51,
        50,
        631,
        593,
        857,
        627,
        312,
        886,
        214,
        355,
        512,
        50,
        412,
        479,
        610,
        969,
        189,
        274,
        355,
        641,
    ]
    print(solution(k, a))
