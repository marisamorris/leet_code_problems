"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""
from collections import Counter

def longestPalindrome(s):
    flag = True
    result = 0
    values = Counter(s)

    for key, value in values.items():
        if value % 2 != 0:
            result += value - 1
            flag = False
        else:
            result += value

    # if flag == True:
    #     return result
    # else:
    #     result += 1
    # return result

    # if flag is TRUE then return result. If FALSE, +1 to result and return
    return result if flag else result + 1



s = "abccccdd"
longestPalindrome(s)
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

s = "a"
# longestPalindrome(s)
# Output: 1

s = "bb"
# longestPalindrome(s)
# Output: 2
