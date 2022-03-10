''' Leetcode 217. Contains Duplicate
Given an integer array 'nums', return 'True' if any value appears at least twice in the array, and return 'False' if
every element is distinct.
'''
def containsDuplicate(nums):
    hash_map = {}
    for i, num in enumerate(nums):

        if num in hash_map.keys():
            return True

        hash_map[num] = i
    return False

def main():
    print(containsDuplicate(nums=[1,2,3,1]))
    print(containsDuplicate(nums=[1,2,3,4]))

if __name__ == '__main__':
    main()