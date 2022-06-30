"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

"""

def repeatedSubstringPattern(s):

    l = len(s) // 2
    sub = ""

    for i in range(l):
        sub += s[i]
        multiplier = len(s) // len(sub)

        # this multiplies the sub sting by the multipler to see if that is the same as s
        if multiplier * sub == s: print(True)
        if multiplier * sub == s: return True

    print(False)
    return False




s = "abab"
# repeatedSubstringPattern(s)
# Output: true
# Explanation: It is the substring "ab" twice.

s = "aba"
# repeatedSubstringPattern(s)
# Output: false


s = "abcabcabcabc"
repeatedSubstringPattern(s)
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.



# data = {}
#
# for char in s:
#     if char not in data:
#         data[char] = 1
#     else:
#         data[char] += 1
#
# lst_values = []
# for key, value in data.items():
#     lst_values.append(value)
#
# print(set(lst_values))
#
# print(len(set(lst_values)) == 1)
# # return len(set(lst_values)) == 1
