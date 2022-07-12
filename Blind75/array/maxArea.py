"""
11. Container With Most Water (medium)

You are given an integer array 'height' of length 'n'. There are 'n' vertical lines drawn such that the two endpoints

of the i-th line are '(i, 0)' and '(i, height[i])'.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

--> Return the maximum amount of water(area) a container can store.

Notice that you may not slant the container.

"""

# O(n*n) exceeds time limit on LeetCode
def maxAreaBruteForce(height: list[int]) -> int:
    ''' two pointer-problem with two nested loops, each moving over the height list'''
    # initialize result var
    result = 0

    # move left and right pointer through height list
    for left_pointer in range(len(height)): # start 0, end at length of array
        for right_pointer in range(left_pointer+1, len(height)): # start at 1, end at length (0 area if both pointers same)

            # calculate area and update result var
            area = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
            result = max(result, area)

    return result


# O(n) linear time
def maxArea(height: list[int]) -> int:
    '''two pointer problem with  starting from left and right (ends of 'height' list) -> max distance,
    then always thake the minimum height of a pair of heights and move pointers inward'''
    # initialize result var
    result = 0

    # initialize pointers at ends of heights
    left_pointer, right_pointer = 0, len(height) - 1

    while left_pointer < right_pointer:

        # calculate area and update result var
        area = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
        result = max(result, area)

        # update pointers
        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return result


def main():
    print('Brute Force O(n*n)')
    print(maxAreaBruteForce(height=[1,8,6,2,5,4,8,3,7]), 'expected: 49')
    print(maxAreaBruteForce(height=[1,1]), 'expected: 1')

    print('\nO(n)')
    print(maxArea(height=[1,8,6,2,5,4,8,3,7]), 'expected: 49')
    print(maxArea(height=[1,1]), 'expected: 1')


if __name__ == '__main__':
    main()
