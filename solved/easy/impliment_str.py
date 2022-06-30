"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

def strStr(haystack, needle):
    # The find() method finds the first occurrence of the specified value.
    # The find() method returns -1 if the value is not found.



    print(haystack.find(needle))
    return haystack.find(needle)





haystack = "hello"
needle = "ll"
# Output: 2
strStr(haystack, needle)

haystack = "aaaaa"
needle = "bba"
# Output: -1
strStr(haystack, needle)
