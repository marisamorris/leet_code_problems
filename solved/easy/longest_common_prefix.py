"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(strs):
    idx = 0

    for i in zip(*strs):
        # print(i)
        if len(set(i)) == 1:
            idx += 1
        else:
            break

    print(strs[0][:idx])
    return strs[0][:idx]


strs = ["flower","flow","flight"]
longestCommonPrefix(strs)
# Output: "fl"

strs = ["dog","racecar","car"]
longestCommonPrefix(strs)
# Output: ""
# Explanation: There is no common prefix among the input strings.
