"""
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
"""
def firstPalindrome(words):
    print(words)

    for word in words:
        if word == word[::-1]:
            # print(word)
            return word

    return ""



words = ["abc","car","ada","racecar","cool"]
firstPalindrome(words)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.


words = ["notapalindrome","racecar"]
firstPalindrome(words)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
#

words = ["def","ghi"]
firstPalindrome(words)
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.
