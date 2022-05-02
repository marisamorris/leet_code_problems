""" MEDIUM
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 """
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
from collections import Counter

def singleNumber(nums):
    print(nums)

    hash = Counter(nums)
    print(hash)

    for k, v in hash.items():
        if v == 1:
            print(k)
            return k

    # for key in hash.keys():
    #     if hash[key] == 1:
    #         print(key)
    #         return key



nums = [2,2,3,2]
singleNumber(nums)
# Output: 3

print("~~~~~~~~~~~~~~~~~~~~" * 2)

nums = [0,1,0,1,0,1,99]
singleNumber(nums)
# Output: 99
