"""
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
"""
from collections import Counter

def uncommonFromSentences(s1, s2):
    # convert strinfs to lists of words
    s1_list = s1.split()
    s2_list = s2.split()

    # get the counts of all the words
    s1_counts = Counter(s1.split())
    s2_counts = Counter(s2.split())

    results = []

    for word in s1_list:
        if s1_counts[word] == 1 and word not in s2_list:
            results.append(word)

    for word in s2_list:
        if s2_counts[word] == 1 and word not in s1_list:
            results.append(word)

    print(results)
    return results




s1 = "this apple is sweet"
s2 = "this apple is sour"
# Output: ["sweet","sour"]
uncommonFromSentences(s1, s2)

print("- - - - - - - - - - - - - - - - -")


s1 = "apple apple"
s2 = "banana"
# Output: ["banana"]
uncommonFromSentences(s1, s2)
