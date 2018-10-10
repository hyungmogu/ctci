# Implement a Queue data structure using two stacks
# *Do Not* create an array inside of Queue class.
# Queue should implement the methods 'enqueue', 'dequeue',
# and 'peek'.

import stack as s

class Queue:
    def __init__(self):
        self.stack1 = s.Stack()
        self.stack2 = s.Stack()

    def enqueue(self, e):
        self.stack1.push(e)

    def dequeue(self):
        while self.stack1.peek() is not None:
            popedE = self.stack1.pop()
            self.stack2.push(popedE)

        # pop the last element of the second stack
        output = self.stack2.pop()

        # put everything back
        while self.stack2.peek() is not None:
            popedE = self.stack2.pop()
            self.stack1.push(popedE)

        return output

    def peek(self):
        while self.stack1.peek() is not None:
            popedE = self.stack1.pop()
            self.stack2.push(popedE)

        # peek the last element of the second stack
        output = self.stack2.peek()

        # put everything back
        while self.stack2.peek() is not None:
            popedE = self.stack2.pop()
            self.stack1.push(popedE)

        return output
