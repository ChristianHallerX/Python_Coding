'''
3. Longest Substring Without Repeating Characters
Given a string 's', find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s: str) -> int:
    # character: index
    hash_map = {}
    # start is a pointer for the start of a substring
    start = 0
    # maxlen is the variable we want to return, initialize at 0
    maxlen = 0

    for i, char in enumerate(s):
        # 1 if char in hash_map, reset start pointer
        if char in hash_map and start <= hash_map[char]:
            start = hash_map[char]+1
        # 2 if char is not in hash_map, recalculate maxlen as difference from start pointer to current index
        else:
            maxlen = max(maxlen, i-start+1) # add one since we're 0-indexed to get len

        # 3 update hash_map
        hash_map[char] = i
    return maxlen


def main():
    print(lengthOfLongestSubstring(s="abcabcbb"), 'expected 3')
    print(lengthOfLongestSubstring(s="bbbbb") ,'expected 1')
    print(lengthOfLongestSubstring(s="pwwkew"), 'expected 3')

if __name__ == '__main__':
    main()