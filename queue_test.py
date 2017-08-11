from queue import Queue

q = Queue()

q.enqueue('boo')
q.enqueue(1)
q.enqueue('good')

print(q.size())
while not q.isEmpty():
    print(q.dequeue())
print(q.size())
# print(output)
