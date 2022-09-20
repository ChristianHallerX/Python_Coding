"""
20. Valid Parentheses (easy)

Given a string 's' containing just the six parentheses characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(s: str) -> bool:
    # time complexity O(n), scan through input string once
    # space complexity O(n), stack could be in worst case as long as input string
    # look at the closing parentheses, check hash map which is the corresponding char, is that char on top of stack?
    # empty list/stack -> all parentheses match each other in correct order -> return True

    # stack is a list for the opening p., appended to the right, last in first out (LIFO)
    stack = []
    # hash map that matches closing parentheses (key) to open parentheses (value)
    close_to_open_dict = {")": "(",
                          "}": "{",
                          "]": "["
                          }
    # loop through string once
    for char in s:
        # if char is a dict key (closing p.) -> find open p. on top of stack (end of list)
        if char in close_to_open_dict:
            # if stack not empty and last item on stack matches the current char's open p.->pop last stack item/open p.
            if len(stack) != 0 and stack[-1] == close_to_open_dict[char]:
                # pop removes last item (-1) by default
                stack.pop()
            else:
                # the last stack element/open p. does not match the open p. or stack is emtpy
                return False
        else:
            # char is not in dict -> is open p. -> append to end of list
            stack.append(char)

    # if all open/closing p. match, then the stack should be empty
    return True if len(stack) == 0 else False


def isValidClean(s: str) -> bool:
    stack = []
    close_to_open_dict = {")": "(",
                          "}": "{",
                          "]": "["
                          }
    for char in s:
        if char in close_to_open_dict:
            if len(stack) != 0 and stack[-1] == close_to_open_dict[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if len(stack) == 0 else False


def main():
    print(isValid(s="()"), "expected True")
    print(isValid(s="()[]{}"), "expected True")
    print(isValid(s="(]"), "expected False")
    print(isValid(s="([)]"), "expected False")


if __name__ == "__main__":
    main()
