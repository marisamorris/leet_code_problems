"""
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.
"""

def twoSumLessThanK(nums, k):
    result = 0

    for i in range(len(nums)):
        for j in range(i + 1, (len(nums))):
            total = nums[i] + nums[j]

            if total > result and total < k:
                result = total

    if result > 0:
        return result
    else:
        return -1

nums = [34,23,1,24,75,33,54,8]
k = 60
twoSumLessThanK(nums, k)
# Output: 58
# Explanation: We can use 34 and 24 to sum 58 which is less than 60.


nums = [10,20,30]
k = 15
twoSumLessThanK(nums, k)
# Output: -1
# Explanation: In this case it is not possible to get a pair sum less that 15.
