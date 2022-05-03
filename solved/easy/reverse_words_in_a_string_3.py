"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""


def reverseWords(s):
    # convert string to list
    s = s.split(" ")
    print(s)

    result = []
    for word in s:
        result.append(word[::-1])

    result = " ".join(result)
    print(result)
    return result






s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
reverseWords(s)

s = "God Ding"
# Output: "doG gniD"
# reverseWords(s)
