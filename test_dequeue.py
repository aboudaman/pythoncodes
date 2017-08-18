from dequeue import Dequeue

test_deq = [2, 3, 4, 5]

test_deq.pop()

print(test_deq)
print("Adding to the front")
test_deq.append(8)
print(test_deq)

print("Add to rear at index 0")
test_deq.insert(0, 10)

print(test_deq)
