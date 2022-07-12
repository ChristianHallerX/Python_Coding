'''
238. Product of Array Except Self

Given an integer array 'nums', return an array 'answer' such that 'answer[i]' is equal to the product of all the

elements of 'nums' except 'nums[i]'.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''

def productExceptSelf(nums: list[int]) -> list[int]:
    ''' Intuition:
    forward pass for the prefix (elements before n[i]), result list becomes prefix
    backward pass for postfix (ele after n[i]), result list (prefix) multiplied with postfix
    '''

    # initialize the output list with 1s
    res = [1] * (len(nums))
    res = [1] * (len(nums))

    prefix = 1
    # forward pass
    for i, _ in enumerate(nums):
        # store prefix in result
        res[i] = prefix
        # update prefix, *= ensures that the multiplication adds up across the pretfix
        prefix *= nums[i]

    postfix = 1
    # backward pass
    for i, _ in reversed(list(enumerate(nums))):
        # multiply prefix with postfix
        res[i] *= postfix
        # update postfix, *= ensures that the multiplication adds up across the postfix
        postfix *= nums[i]
    return res


def main():
    print(productExceptSelf(nums=[1,2,3,4]), 'expected output = [24,12,8,6]')
    print(productExceptSelf(nums=[-1,1,0,-3,3]), 'expected output = [0,0,9,0,0]')


if __name__ == '__main__':
    main()
