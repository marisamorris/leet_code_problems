"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

def maxSubArray(nums):

    if len(nums) == 1: return nums[0]

    working_max = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):

        working_max = max(nums[i], working_max + nums[i])
        
        result = max(working_max, result)

    print(result)
    return result



nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
print("~~~~~~~~" * 3)

nums = [1]
maxSubArray(nums)
# Output: 1
print("~~~~~~~~" * 3)

nums = [5,4,-1,7,8]
maxSubArray(nums)
# Output: 23
print("~~~~~~~~" * 3)

nums = [-2,-1]
maxSubArray(nums)
