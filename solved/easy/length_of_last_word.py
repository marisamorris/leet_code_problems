"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

def lengthOfLastWord(s):
    # Solution1
    # split on the spaces in the string
    s = s.split(" ")
    #join on empty idx and split again to get rid of them
    s = " ".join(s).split()

    return len(s[-1])

    # Solution2
    # new_string = s.split(" ")
    #     # print(new_string)
    # for index in reversed(new_string):
    #     # print(index)
    #     if len(index) > 0: return len(index)


s = "Hello World"
lengthOfLastWord(s)
# Output: 5
# Explanation: The last word is "World" with length 5.

print("------------------------------------------")

s = "   fly me   to   the moon  "
lengthOfLastWord(s)
# Output: 4
# Explanation: The last word is "moon" with length 4.


s = "luffy is still joyboy"
# lengthOfLastWord(s)
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
