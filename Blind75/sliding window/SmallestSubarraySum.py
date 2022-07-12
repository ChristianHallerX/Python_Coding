#  Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray
#  whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists. Sliding window not fixed.

def smallestSubarraySum(S, arr):

    return



def main():
    print("Length smallest contiguous subarray greater S: " + str(
        ssmallestSubarraySum(7, [2, 1, 5, 2, 3, 2])) + " " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]) == 2))

    print("Length smallest contiguous subarray greater S: " + str(
        smallestSubarraySum(7,[2, 1, 5, 2, 8])) + " " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]) == 1))

    print("Length smallest contiguous subarray greater S: " + str(
        smallestSubarraySum(8, [2, 1, 5, 2, 3, 2])) + " " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2]) == 3))

if __name__ == "__main__":
    main()
