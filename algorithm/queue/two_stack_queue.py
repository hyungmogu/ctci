import sys

import queue as q

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Obtain the value of q
q = int(sys.stdin.readline().strip())

# Obtain the value of head
j = 0
keep_going = True
while keep_going:
    j +=1

    query = sys.stdin.readline().strip().split()
    if query[0] == '1':
        queue = q.Queue(int(query[1]))
        keep_going = False



# Read two elements in the input
while j < q:
    query = sys.stdin.readline().strip().split()
    # enqueue element if the value of query is 1
    if query[0] == '1':
        queue.enqueue(int(query[1]))
    # dequeue if the value of query is 2
    elif query[0] == '2':
        queue.dequeue()
    # peek if the value of query is 3
    elif query[0] == '3':
        print(queue.peek())
    j += 1



