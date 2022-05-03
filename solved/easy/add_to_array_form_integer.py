"""
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
"""
def addToArrayForm(num, k):
    # convert each int in array to a string. becomes list of strings
    num = [str(int) for int in num]
    print(num)

    # join the the string list
    num = "".join(num)

    # add num and K together
    num = str(int(num) + k)

    # convert result back into list
    num = [int(char) for char in num]

    # print(num)
    return num









num = [1,2,0,0]
k = 34
# # Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
addToArrayForm(num, k)
print("- - - - - - - - - -")


num = [2,7,4]
k = 181
# # Output: [4,5,5]
# Explanation: 274 + 181 = 455
addToArrayForm(num, k)
print("- - - - - - - - - -")


num = [2,1,5]
k = 806
# # Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
addToArrayForm(num, k)
