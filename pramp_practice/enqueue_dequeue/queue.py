#
# Queue
#
#   Create a queue data structure. The queue should be a class
#   with methods enqueue and dequeue. Adding to the queue should
#   store an element until it is removed.
#
#   -- Example (queue)
#       q = Queue() -- q.queue = []
#
#   -- Example (enqueue)
#       q = Queue()
#       q.enqueue(1) -- [1]
#       q.enqueue(2) -- [2,1]
#   -- Example (dequeue)
#       [2,1]
#       q.dequeue() // returns 1 && [2]
#       q.dequeue() // returns 2 && []
#       q.dequeue() // ValueError
#
#   -- [1,2]
#   -- q.peak() --

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, n):
        self.queue = [n] + self.queue

    def dequeue(self):
        if len(self.queue) == 0:
            raise ValueError

        output = self.queue.pop()
        return output

    def peek(self):
        if len(self.queue) == 0:
            raise ValueError

        return self.queue[-1]
