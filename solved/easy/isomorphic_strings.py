"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

"""
def isIsomorphic(s, t):
    # convert each string to a list
    s_list = [char for char in s]
    t_list = [char for char in t]
    print(s_list)
    print(t_list)

    # zip up the lists and convert to list
    zipped_list = list(zip(s_list, t_list))
    print(zipped_list)


    # convert to a set to get rid of duplicates
    set_list = set(zipped_list)
    print(set_list)

    # compare the lenght of the set list and zipped list
    if len(set_list) == len(zipped_list):
        print(False)
        return False

    print(True)
    return True


s = "ab"
t = "ab"
isIsomorphic(s, t)
# Output: true
print("- - - - - - - - - - - - - - - - - -")

# s = "egg"
# t = "add"
# isIsomorphic(s, t)
# # Output: true
# print("- - - - - - - - - - - - - - - - - -")
#
# s = "foo"
# t = "bar"
# isIsomorphic(s, t)
# # Output: false
# print("- - - - - - - - - - - - - - - - - -")
#
# s = "paper"
# t = "title"
# isIsomorphic(s, t)
# # Output: true
