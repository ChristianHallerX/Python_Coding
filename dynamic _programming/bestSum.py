'''
Write a function 'bestSum(targetSum, numbers)' that takes in a 'targetSum' and a list of 'numbers' as arguments.

The function should return a list containing the shortest combination of numbers that add up exactly the targetSum.

If there is a tie for the shortest combination, you can return any of the shortest.

# we have to search the entire recursion tree for the shortest result
'''

def bestSum(targetSum, numbers, dict=None):
    if dict == None:
        dict = {}
    # load from dict and shortcut if possible
    if targetSum in dict.keys():
        return dict[targetSum]
    # base case 1
    if targetSum == 0:
        return []
    # base case 2
    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, dict)
        if remainderCombination is not None:
            # we need a copy to point at a new place in memory, or else Python mutates the list
            remainderCombination = remainderCombination.copy()
            remainderCombination.append(num)
            # if the combination is shorter than the current shortest, then update. First time, shortest combo is None
            if (shortestCombination == None) or (len(remainderCombination) < len(shortestCombination)):
                shortestCombination = remainderCombination.copy()

    dict[targetSum] = shortestCombination
    return shortestCombination


def main():
    print(bestSum(targetSum=7, numbers=[5,2,4,7])) # [7]
    print(bestSum(targetSum=8, numbers=[2,3,5])) # [3, 5]
    print(bestSum(targetSum=8, numbers=[1,4,5]))  # [4, 4]
    print(bestSum(targetSum=100, numbers=[2, 3, 5, 25]))  # [25,25,25,25]
    print(bestSum(300, [2, 7]))


if __name__ == '__main__':
    main()
