"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

def subsets(nums):
    print(nums)

    results = [[]]

    for num in nums:

        results += [i + [num] for i in results]

    print(results)
    return results



nums = [1,2,3,4]
subsets(nums)
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

nums = [0]
# subsets(nums)
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.


# if temp.sort() not in subsets:
