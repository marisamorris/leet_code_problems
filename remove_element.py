"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

def removeElement(nums, val):
    i = len(nums) - 1

    while i >= 0:
        if nums[i] == val:
            nums.pop(i)
        i -= 1

    print(len(nums))

    # solution 2
    # count = 0
    #
    # for i in range(len(nums)):
    #     if nums[i] != val :
    #         nums[count] = nums[i]
    #         count +=1
    #
    # print(count)
    # return count





nums = [3,2,2,3]
val = 3
removeElement(nums, val)

# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums, val)
# Output: 5, nums = [0,1,4,0,3,_,_,_]
