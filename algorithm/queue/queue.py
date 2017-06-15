class Queue():
    def __init__(self,head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def dequeue(self):

        if len(self.storage) == 0:
            return

        return self.storage.pop(0)

    def peek(self):
        return self.storage[0]