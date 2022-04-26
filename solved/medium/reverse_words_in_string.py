""" MEDIUM
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

"""

def reverseWords(s):
    # print(s)

    # split the string on each space and turn to list (there will be empty strings in list)
    str_list = s.split(" ")

    # join on the spaces to create a string and spit again to make a list
    str_list = ' '.join(str_list).split()
    print(str_list)

    i = 0
    l = len(str_list) - 1

    while i < l:
        temp = str_list[i]

        str_list[i] = str_list[l]
        str_list[l] = temp

        i += 1
        l -= 1

    # join agian on spaces to create string
    s = ' '.join(str_list)


    print(s)
    return s






s = "the sky is blue"
reverseWords(s)
# Output: "blue is sky the"

s = "  hello world  "
reverseWords(s)
# # Output: "world hello"
# # Explanation: Your reversed string should not contain leading or trailing spaces.

s = "a good   example"
reverseWords(s)
# # Output: "example good a"
# # Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
