"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

def subsetsWithDup(nums):
    results = [[]]

    for num in nums:
        for result in list(results):
            temp = sorted(result + [num])

            if temp not in results:
                results.append(temp)

    print(results)
    return results




nums = [1,2,2]
subsetsWithDup(nums)
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

nums = [0]
subsetsWithDup(nums)
# Output: [[],[0]]


# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
