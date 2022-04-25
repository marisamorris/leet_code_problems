"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

def searchInsert(nums, target):
    if target in nums: return nums.index(target)

    for index, num in enumerate(nums):
        print(index, num)

        if num >= target:
            return index

    return len(nums)










nums = [1,3,5,6]
target = 5
searchInsert(nums, target)
print("-------------------")
# Output: 2

nums = [1,3,5,6]
target = 2
searchInsert(nums, target)
print("-------------------")
# Output: 1

nums = [1,3,5,6]
target = 7
searchInsert(nums, target)
# Output: 4





















    #
    # if target in nums: print(nums.index(target))
    # if target in nums: return nums.index(target)
    #
    # # i = 0
    #
    # for index, num  in enumerate(nums):
    #     # print(index, num)
    #
    #     if num >= target:
    #         print(index)
    #         return index
    #
    # print(len(nums))
    # return len(nums)
