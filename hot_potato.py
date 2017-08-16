from queue import Queue
import random

hot_q = Queue()
num = random.randrange(1, 20)
turn = 0
hot_q.enqueue('Abou')
hot_q.enqueue('Paul')
hot_q.enqueue('Sophie')
hot_q.enqueue('Christian')
hot_q.enqueue('Gary')
hot_q.enqueue('Alex')

print(hot_q.size())
print(f"Turn Before is {turn}")

while not hot_q.size() <= 1:
    # print("Inside While")
    if turn == num:
        hot_q.dequeue()
        turn = 0
    else:
        hot_q.enqueue(hot_q.dequeue())
        turn += 1


print(f"Size after {hot_q.size()}")
print(f"Turn After is {turn}")
print(f"Last person left is {hot_q.dequeue()}")
