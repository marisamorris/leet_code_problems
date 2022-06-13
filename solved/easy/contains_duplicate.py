"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""

def containsDuplicate(nums):
    data = {}

    for num in nums:
        if num in data:
            data[num] += 1
        else:
            data[num] = 1

    for key, value in data.items():
        if value > 1:
            return True

    return False

nums = [1,2,3,1]
containsDuplicate(nums)
# Output: true

nums = [1,2,3,4]
containsDuplicate(nums)
# Output: false

nums = [1,1,1,3,3,4,3,2,4,2]
containsDuplicate(nums)
# Output: true
