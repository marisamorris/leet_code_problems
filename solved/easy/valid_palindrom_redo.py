"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

def isPalindrome(s):
    s = s.lower()
    s_list = list(s)
    l = len(s_list) - 1

    while l >= 0:
        if s_list[l].isalnum() == False:
            s_list.pop(l)

        l -= 1

    print(s_list == s_list[::-1])
    return s_list == s_list[::-1]


s = "A man, a plan, a canal: Panama"
isPalindrome(s)
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = "race a car"
isPalindrome(s)
# Output: false
# Explanation: "raceacar" is not a palindrome.

s = " "
isPalindrome(s)
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
