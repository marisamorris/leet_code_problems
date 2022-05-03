"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

def reverseString(s):
    i = 0
    l = len(s) - 1

    while i <= l:
        temp = s[i]

        s[i] = s[l]
        s[l] = temp

        i += 1
        l -= 1

    print(s)
    return s

s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
reverseString(s)


s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
reverseString(s)
