import operator

class Stack:
    def init(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, val):
        return self.items.insert(0, val)

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]


A = ['1','2','+','3','*']


class Solution:
    def evalRPN(self, A):
        operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
        stack = Stack()

        for i in A:
            if i not in operators.keys():
                stack.push(i)
            else:
                if stack.size()<2:
                    return False
                else:
                    n1 = int(stack.pop())
                    n2 = int(stack.pop())
                    val = operators[i](n2,n1)
                    stack.push(val)

        return int(stack.peek())
