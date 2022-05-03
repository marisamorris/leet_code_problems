"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""

def rotateString(s, goal):
    print(s, goal)

    # edge cases
    if len(s) != len(goal): return False
    if len(s) == 0: return True

    # add string to string to see if goal can be found in it.
    s = s + s
    print(s)

    print(goal in s)
    return goal in s


s = "abcde"
goal = "cdeab"
# Output: true
rotateString(s, goal)

print("- - - - - - - -")

s = "abcde"
goal = "abced"
# Output: false
rotateString(s, goal)
