# --- Directions
# 2) implement the weave function. Weave
# receives two queues as arguements and combines the
# contents of each into a new, third queue. The third
# queue should contain the *alternating* content
# of the two queues. The function should handle
# queues of different lengths without inserting
# undefined into the new one.
#
# -- Example
#  queue = Queue()
#  queue.enqueue(1)
#  queue.enqueue(2)
#  ------------
#  [2,1]
#
#  queue2 = Queue()
#  queue2.enqueue(3)
#  queue2.enqueue(4)
#  ------------
#  [4,3]
#
#
# weave(queue, queue2) --> [4,2,3,1]
#
# queue3 = Queue()
# queue3.enqueue(1)
# queue3.enqueue(2)
# queue3.enqueue(3)
# queue3.enqueue(4)
# queue3.enqueue(5)
# queue3.enqueue(6)
# queue3.enqueue(7)
# ----------------
# [7,6,5,4,3,2,1]

# queue4 = Queue()
# queue4.enqueue(8)
# queue4.enqueue(9)
# queue4.enqueue(10)
# ==================
# [10,9,8]

# weave(queue3, queue4) --> [7,6,5,4,10,3,9,2,8,1]

# input
#  - object Queue
# output
#  - object Queue
import queue as q

def weave(queue1, queue2):
    output = q.Queue()

    if not isinstance(queue1, q.Queue) or not isinstance(queue2, q.Queue):
        raise TypeError

    if queue1.peek() == None and queue2.peek() == None:
        raise ValueError

    while not both_queues_are_empty(queue1, queue2):
        try:
            value1 = queue1.dequeue() #1
            output.enqueue(value1) #[2,3,1]
        except:
            pass

        try:
            value2 = queue2.dequeue() #3
            output.enqueue(value2) #[4,2,3,1]
        except:
            pass

    return output

def both_queues_are_empty(queue1, queue2):
    if queue1.peek() == None and queue2.peek() == None:
        return True
    return False


