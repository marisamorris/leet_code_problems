"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(i, j)
                return i, j



nums = [2,7,11,15]
target = 9
twoSum(nums, target)
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [3,2,4]
target = 6
twoSum(nums, target)
# Output: [1,2]

nums = [3,3]
target = 6
twoSum(nums, target)
# Output: [0,1]
