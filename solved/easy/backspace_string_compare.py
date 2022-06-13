"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""


def backspaceCompare(s, t):
    print(s, t)
    s_list = []
    t_list = []

    for char in s:
        if char != "#":
            s_list.append(char)
        elif char == "#":
            s_list.pop()

    for char in t:
        if char != "#":
            t_list.append(char)
        elif char == "#":
            t_list.pop()

    # print(s_list == t_list)
    # return True if s_list == t_list else False
    return s_list == t_list




s = "ab#c"
t = "ad#c"
backspaceCompare(s, t)
# Output: true
# Explanation: Both s and t become "ac".


s = "ab##"
t = "c#d#"
# backspaceCompare(s, t)
# Output: true
# Explanation: Both s and t become "".


s = "a#c"
t = "b"
# backspaceCompare(s, t)
# Output: false
# Explanation: s becomes "c" while t becomes "b".





































    # s_list = []
    # t_list = []
    #
    # for char in s:
    #     if char != "#":
    #         s_list.append(char)
    #     elif char == "#" and s_list:
    #         s_list.pop()
    #
    # for char in t:
    #     if char != "#":
    #         t_list.append(char)
    #     elif char == "#" and t_list:
    #         t_list.pop()
    #
    # print(True) if s_list == t_list else print(False)
    # return True if s_list == t_list else False
