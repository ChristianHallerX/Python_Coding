'''
217. Contains Duplicate
Given an integer array 'nums', return 'True' if any value appears at least twice in the array,
and return 'False' if every element is distinct.
'''

def containsDuplicate(nums):
    hash_map = {}
    for i, num in enumerate(nums):
        # check if current element (num) is in hash_map, finish function and return True
        if num in hash_map.keys():
            return True

        # if num not in hash_map, write to hash_map
        hash_map[num] = i
    return False

def main():
    print(containsDuplicate(nums=[1,2,3,1]), 'expected: True')
    print(containsDuplicate(nums=[1,2,3,4]), 'expected: False')
    print(containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]), 'expected: True')

if __name__ == '__main__':
    main()