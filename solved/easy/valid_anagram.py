"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""





def isAnagram(s, t):
    s = sorted(list(s))
    t = sorted(list(t))

    print(s == t)
    return s == t



s = "anagram"
t = "nagaram"
isAnagram(s, t)
# Output: true

s = "rat"
t = "car"
isAnagram(s, t)
# Output: false
