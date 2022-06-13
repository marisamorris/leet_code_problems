"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

majority element appears more than ⌊n / 2⌋ times
"""


def majorityElement(nums):
    comparison = len(nums) / 2
    output = 0

    data = {}

    for i in nums:
        if i not in data:
            data[i] = 1
        else:
            data[i] += 1

    for k, v in data.items():
        if v > comparison and v >= output:
            output = k
            print(output)
            return output


nums = [3,2,3]
majorityElement(nums)
# Output: 3


nums = [2,2,1,1,1,2,2]
majorityElement(nums)
# Output: 2
