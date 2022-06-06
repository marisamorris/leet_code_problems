"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

"""


def prefixCount(words, pref):
    # use string slicing and then iterate throught the words list
    result = 0

    for word in words:

        if word[0:len(pref)] == pref:
            result += 1

    print(result)
    return result





words = ["pay","attention","practice","attend"]
pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
prefixCount(words, pref)


words = ["leetcode","win","loops","success"]
pref = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.
prefixCount(words, pref)
