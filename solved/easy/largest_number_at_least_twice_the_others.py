"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
"""

def dominantIndex(nums):

    for k, v in enumerate(nums):

        if (nums.index(max(nums)) != k) & (v * 2 > max(nums)):
            return -1

    print(nums.index(max(nums)))
    return nums.index(max(nums))




nums = [3,6,1,0]
# Output: 1
dominantIndex(nums)
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.

print("- - - - - - - - - - - - ")

nums = [1,2,3,4]
# Output: -1
dominantIndex(nums)
# Explanation: 4 is less than twice the value of 3, so we return -1.

print("- - - - - - - - - - - - ")

nums = [1]
# Output: 0
dominantIndex(nums)
# Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.
