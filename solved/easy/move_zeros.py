"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

def moveZeroes(nums):
    if len(nums) <= 1: return nums

    counter = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            # counter is always keeping track of the index with a 0
            nums[counter], nums[i] = nums[i] , nums[counter]
            counter += 1

    print(nums)
    return nums



nums = [0,1,0,3,12]
moveZeroes(nums)
# Output: [1,3,12,0,0]


nums = [0]
moveZeroes(nums)
# Output: [0]
