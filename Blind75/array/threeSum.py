'''
15. 3Sum (medium)

Given an integer array 'nums', return all the triplets [nums[i], nums[j], nums[k]] such that

i != j
i != k
j != k

and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''


def threeSum(nums: list[int]) -> list[List[int]]:
    ''' First, sort the nums list, fix the first number (negative), get difference to 0, then use two-pointer
    algorithm of TwoSumII to find the two values that add up to the difference.'''
    result = [] # initialize the output

    # sort the input list
    nums.sort()

    for index, value in enumerate(nums):
        # skip if the second value is the same as the first (there may be duplicates in nums,
        # but we don't want duplicates in the result)
        if index>0 and value == nums[index-1]:
            continue
        else:


            # for starting at second index, twoSumII solution, initialize left/right index pointers
            left_pointer, right_pointer = 0+1, len(nums)-1
            while left_pointer < right_pointer:
                # make sum of three values and evaluate how pointers need to be moved
                threeSum = value + nums[left_pointer] + nums[right_pointer]

                if threeSum > 0:
                    right_pointer -= 1
                elif threeSum <0:
                    left_pointer += 1
                else:
                    # if sum == 0, then append this combination to result
                    result.append([value, nums[left_pointer], nums[right_pointer]])

                    # next, move left pointer
                    left_pointer += 1
                    while nums[left_pointer] == nums[left_pointer -1] and left_pointer < right_pointer:
                        left_pointer += 1
    return result


def main():
    print(threeSum(nums=[-1,0,1,2,-1,-4]), "expected: [[-1,-1,2],[-1,0,1]]")
    print(threeSum(nums=[]), "expected: []")
    print(threeSum(nums=[0]), "expected: []")


if __name__ == '__main__':
    main()