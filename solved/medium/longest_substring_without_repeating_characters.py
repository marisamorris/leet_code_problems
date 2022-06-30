"""
Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s):
    # print(s)
    result = 0
    working_sub = ""

    for i in range(len(s)):

        if s[i] not in working_sub:
            working_sub += s[i]

        else:
            # compare the length of working sub to result and set result to max
            result = max(result, len(working_sub))

            # this finds the index of the s[i] in the working sub and adds one THEN sets working_sub to that to working_sub starting at s[i]+1 to the end of the working_sub string
            working_sub = working_sub[working_sub.index(s[i]) + 1:]

    result = max(result, len(working_sub))



s = "abcabcbb"
lengthOfLongestSubstring(s)
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example

# print("-----------------")

s = "bbbbb"
# lengthOfLongestSubstring(s)
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example

# print("-----------------")

s = "pwwkew"
# lengthOfLongestSubstring(s)
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
