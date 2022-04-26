"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

def isPalindrome(x):

    # convert to string
    new_string = str(x)
    return True if new_string == new_string[::-1] else False


x = 121
isPalindrome(x)
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

x = -121
isPalindrome(x)
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

x = 10
isPalindrome(x)
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
