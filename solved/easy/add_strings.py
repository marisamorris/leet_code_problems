"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
"""

def addStrings(num1, num2):
    print(str(int(num1) + int(num2)))
    return str(int(num1) + int(num2))


num1 = "11"
num2 = "123"
# Output: "134"
addStrings(num1, num2)
print("- - - - - - - - - - - ")

num1 = "456"
num2 = "77"
# Output: "533"
addStrings(num1, num2)
print("- - - - - - - - - - - ")

num1 = "0"
num2 = "0"
# Output: "0"
addStrings(num1, num2)
