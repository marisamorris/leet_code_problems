"""
https://leetcode.com/problems/string-compression/
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""

# the excess characters can be deleted

# def compress(chars):
#     if len(chars) == 1: chars.append("1")
#     return chars

def compress(chars):
    # if len(chars) == 1: chars.append("1")
    if len(chars) == 1: return len(chars)

    values = {}

    for char in chars:
        if char not in values:
            values[char] = 1
        else:
            values[char] += 1

    new = []

    for k, v in values.items():
        if v == 1:
            new.append(k)
            continue

        new.append(k)

        v = str(v)
        if len(v) > 1:
            v_list = list(v)
            for i in v_list:
                new.append(i)
        else:
            new.append(v)

    # print(new)
    # print(len(new))
    print(new)
    return new
    return len(new)





chars = ["a","a","b","b","c","c","c"]
compress(chars)
print("-------" * 3)
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".


chars = ["a"]
compress(chars)
print("-------" * 3)
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
compress(chars)
print("-------" * 3)
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
