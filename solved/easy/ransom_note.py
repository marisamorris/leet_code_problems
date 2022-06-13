"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
from collections import Counter

def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine): return False

    ransomNote_counts = Counter(ransomNote)
    magazine_counts = Counter(magazine)

    for key, count in ransomNote_counts.items():
        magazine_count = magazine_counts[key]
        print(magazine_count)

        if magazine_count < count:
            return False

    return True




ransomNote = "a"
magazine = "b"
canConstruct(ransomNote, magazine)
# Output: false


ransomNote = "aa"
magazine = "ab"
canConstruct(ransomNote, magazine)
# Output: false


ransomNote = "aa"
magazine = "aab"
canConstruct(ransomNote, magazine)
# Output: true
