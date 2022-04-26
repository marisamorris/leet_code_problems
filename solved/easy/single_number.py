"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

"""

def singleNumber(nums):
    hash = {}

    for num in nums:
        if num not in hash:
            hash[num] = 1
        else:
            hash[num] += 1

    for key, value in hash.items():
        if value == 1:
            print(key)
            return key


    print(hash)




nums = [2,2,1]
singleNumber(nums)
# Output: 1
print("~~~~~~~~~~~" * 2)

nums = [4,1,2,1,2]
singleNumber(nums)
# Output: 4
print("~~~~~~~~~~~" * 2)

nums = [1]
singleNumber(nums)
# Output: 1
