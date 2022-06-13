"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(strs):

    index = 0

    for i in zip(*strs):
        if len(set(i)) == 1:
            index += 1
        else:
            break

    print(strs[0][:index])



strs = ["flower","flow","flight"]
longestCommonPrefix(strs)
# Output: "fl"

print("--------------------------------")

strs = ["dog","racecar","car"]
longestCommonPrefix(strs)
# Output: ""
# Explanation: There is no common prefix among the input strings.
