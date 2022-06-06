"""
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
"""
from collections import Counter

def countWords(words1, words2):
    # count occurences of word in dictionaries
    words_dict_1 = Counter(words1)
    words_dict_2 = Counter(words2)

    count = 0

    for k ,v in words_dict_1.items():

        if v == 1:
            if k in words_dict_2 and words_dict_2[k] == 1:
                count += 1

    print(count)
    return count







words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
countWords(words1, words2)
# Output: 2

# Explanation:
# - "leetcode" appears exactly once in each of the two arrays. We count this string.
# - "amazing" appears exactly once in each of the two arrays. We count this string.
# - "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
# - "as" appears once in words1, but does not appear in words2. We do not count this string.
# Thus, there are 2 strings that appear exactly once in each of the two arrays.


words1 = ["b","bb","bbb"]
words2 = ["a","aa","aaa"]
countWords(words1, words2)
# Output: 0
# Explanation: There are no strings that appear in each of the two arrays.


words1 = ["a","ab"]
words2 = ["a","a","a","ab"]
countWords(words1, words2)
# Output: 1
# Explanation: The only string that appears exactly once in each of the two arrays is "ab".
