"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
from collections import Counter

def firstUniqChar(s):
    print(s)

    # get counts of all character occurences
    counts = Counter(s)
    print(counts)

    # iterate through using enumerate to get index and char and check against counts
    for index, char in enumerate(s):
        print(index, char)

        if counts[char] == 1:
            print(index)
            return index

    print(-1)
    return -1


s = "leetcode"
# Output: 0
firstUniqChar(s)
print("- - - - - - - - - - - -")

s = "loveleetcode"
# Output: 2
firstUniqChar(s)
print("- - - - - - - - - - - -")

s = "aabb"
# Output: -1
firstUniqChar(s)
