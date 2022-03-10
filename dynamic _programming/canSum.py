'''
Write a function "canSum(targetSum, numbers)" that takes in a targetSum and array of numbers as arguments.

The function should return a Boolean indicating whether or not it is possible to generate the targetSum using numbers
from the array.

You can use an element of the array as many times as needed.

You may assume that all elements of the array are non-negative.
'''

def canSum(targetSum, numbers):
    # base case 1
    if targetSum == 0:
        return True
    # base case 2
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        # recursively call the same function, but now with remainder
        if canSum(remainder, numbers) == True:
            # bubble up True
            return True
    # if the loop did not return True, only then return False
    return False

# the dict will have targetSum as keys, Boolean as value
def canSumDynamic(targetSum, numbers, dict=None):
    # Python requires this workaround, since the dict gets mutated. Instantiates dict only in first call.
    if dict == None:
        dict = {}

    # short-cut this function call by loading from dict
    if targetSum in dict.keys():
        return dict[targetSum]
    # base case 1
    if targetSum == 0:
        return True
    # base case 2
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        # recursively call the same function, but now with remainder
        if canSumDynamic(remainder, numbers, dict) == True:
            dict[targetSum] = True # write True to dict
            return True
    # if the loop did not return True, only then return False
    dict[targetSum] = False # write False to dict
    return False


def main():
    print('brute forece')
    print(canSum(targetSum=7, numbers=[2,3]))  # True
    print(canSum(targetSum=7, numbers=[5,2,4,7])) # True
    print(canSum(targetSum=7, numbers=[2,4]))  # False
    print(canSum(targetSum=8, numbers=[2,3,5]))  # True
    # this takes very long
    #print(canSum(targetSum=300, numbers=[7,14]))  # False

    print('dynamic')
    print(canSumDynamic(targetSum=7, numbers=[2, 3]))  # True
    print(canSumDynamic(targetSum=7, numbers=[5, 2, 4, 7]))  # True
    print(canSumDynamic(targetSum=7, numbers=[2, 4]))  # False
    print(canSumDynamic(targetSum=8, numbers=[2, 3, 5]))  # True
    print(canSumDynamic(targetSum=300, numbers=[7, 14]))  # False

if __name__ == '__main__':
    main()