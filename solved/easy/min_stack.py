"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
"""


class MinStack:
    def __init__(self):

        self.stack = []

    def push(self, val) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        # print(min(self.stack))
        return min(self.stack)



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(val)
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
