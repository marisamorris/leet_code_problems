"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

def isValid(s):
    if not s: return True

    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        print(stack)
        if char in pairs and stack:
            if stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)

    print(stack == [])
    return stack == []



s = "()"
# isValid(s)
# Output: true

s = "()[]{}"
# isValid(s)
# # Output: true
#
s = "(]"
# isValid(s)
# # Output: false
