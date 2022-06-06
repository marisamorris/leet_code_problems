"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
"""


def reverseStr(s, k):
    s = list(s)

    # range(start, stop, range)
    for i in range(0, len(s), 2 * k):

        s[i:i+k] = reversed(s[i:i+k])

    print("".join(s))
    return "".join(s)





s = "abcdefg"
k = 2
# Output: "bacdfeg"
reverseStr(s, k)

print("- - - - - - - - - - - - -")

s = "abcd"
k = 2
# Output: "bacd"
reverseStr(s, k)
