# --- Directions
# Create a stack data structure. The stack
# should be a class with methods 'push', 'pop', and
# 'peek'. Adding an element to the stack should
# store it until it is removed

# s = Stack()
# s.stack --> []
# -------------
# s.push(1) --> [1]
# s.push(2) --> [1,2]
# LIFO (Last in and First Out)

# s.pop() --> 2, [1]
# s.pop() --> 1, []
# s.pop() --> None, []

# s.peek() --> 2, [1,2]


class Stack:
    def __init__(self):
        self.stack = []

    def push(self,e):
        self.stack.append(e)

    def pop(self):
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None

        return self.stack[-1]