"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

def climbStairs(n):
    one, two = 1 , 1

    for i in range(n - 1):
        print(i)
        temp = one
        one = one + two
        two = temp

    # print(one)
    return one








n = 2
climbStairs(n)
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

print("- - - - - - - - - ")

n = 3
climbStairs(n)
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
