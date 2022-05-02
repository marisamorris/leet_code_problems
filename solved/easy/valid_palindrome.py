"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

def isPalindrome(s):
    # convert to lowercase & list structure
    s = s.lower()
    s_list = list(s)

    # get rid of the spaces
    s_list = " ".join(s_list).split()

    # get rid of chars not alphanumeric
    l = len(s_list) - 1

    while l >= 0:
        if s_list[l].isalnum() == False:
            s_list.pop(l)

        l -= 1

    # print("".join(s_list) == "".join(s_list)[::-1])
    return "".join(s_list) == "".join(s_list)[::-1]


s = "0P"
# s = ".a"
# s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
isPalindrome(s)

s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# isPalindrome(s)

s = " "
# isPalindrome(s)
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
