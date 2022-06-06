"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
"""
from collections import Counter

def kthDistinct(arr, k):
    # use the counter to how many of each element
    counts = Counter(arr)

    print(arr)
    # iterate through array checking elements against counts
    for int in arr:

        # if count of int is only 1 subtract 1 from k
        if counts[int] == 1:
            k -= 1

        # if k is 0 then return the element of where were at in the loop.
        if k == 0: print(int)
        if k == 0: return int

    return ""


arr = ["d","b","c","b","c","a"]
k = 2
kthDistinct(arr, k)
# Output: "a"

# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned.

arr = ["aaa","aa","a"]
k = 1
kthDistinct(arr, k)
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.

arr = ["a","b","a"]
k = 3
kthDistinct(arr, k)
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".


# SOLUTION 2
# hash = {}
#
# for int in arr:
#     if int not in hash:
#         hash[int] = 1
#     else:
#         hash[int] += 1
#
# distinct = []
#
# for key, value in hash.items():
#     if value == 1:
#         distinct.append(key)
#
# if len(distinct) < k: return ""
#
# return distinct[k-1]
