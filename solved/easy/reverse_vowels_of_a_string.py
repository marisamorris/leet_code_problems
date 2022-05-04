"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
"""

def reverseVowels(s):

    # convert s to list and lowercase
    s = list(s)
    print(s)

    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    i = 0
    l = len(s) - 1

    while i < l:
        # check if whats at the i index is a vowel and if not keep going
        if s[i] not in vowels:
            i += 1
            continue

        # check if whats at the l index is a vowel and if not keep going
        if s[l] not in vowels:
            l -= 1
            continue

        # make the switch
        s[i], s[l] = s[l], s[i]
        i += 1
        l -= 1

    # join the list. make a string again and return
    s = "".join(s)

    print(s)
    return s


s = "hello"
# Output: "holle"
# reverseVowels(s)


s = "leetcode"
# Output: "leotcede"
reverseVowels(s)
