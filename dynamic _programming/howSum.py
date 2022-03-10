'''
Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.

The function should return an array containing any combination of elements that add up exactly the targetSum.

If there is no combination that adds up to targetSum, then return None.

If there are multiple combinations possible, then return any single one.
'''

def howSum(targetSum, numbers, dict=None):
    # instantiate dictionary
    if dict == None:
        dict = {}

    # load from dict
    if targetSum in dict:
        return dict[targetSum]

    # base case 1
    if targetSum == 0:
        return []
    # base case 2
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        # in the recursion, enter the entire numbers array again so nums can be re-used
        remainderResult = howSum(remainder, numbers, dict)

        if remainderResult != None:
            # unpack the list and add the num that was subtracted
            remainderResult.append(num)
            dict[targetSum] = remainderResult
            return dict[targetSum]

    # if the for loop did not find a number combination that returned a list -> did not end in targetSum == 0
    dict[targetSum] = None
    return None


def main():
    print(howSum(targetSum=7, numbers=[2, 3]))  # [3, 2, 2]
    print(howSum(targetSum=7, numbers=[5, 3, 4, 7])) # [3, 4], or [7]
    print(howSum(targetSum=7, numbers=[2, 4])) # None
    print(howSum(targetSum=8, numbers=[2, 3, 5])) # [2, 2, 2, 2] or [3, 5]
    print(howSum(targetSum=300, numbers=[7, 14]))  # None takes very long
    print(howSum(targetSum=0, numbers=[1, 2, 3])) # []

if __name__ == '__main__':
    main()