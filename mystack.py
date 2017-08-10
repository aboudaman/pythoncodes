"""
Stack Operations:
    1) isEmpty()
    2) push()
    3) pop()
    4) peek()
    5) size()

"""

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

st = Stack()

print("Is the Stack Empty?", st.isEmpty())
st.push("BooBoo")
print(st.peek())
st.push(5.3)
print(st.peek())

print("The size of the stack is", st.size())
st.pop()
print("The size of the stack is", st.size())
st.push("Aloha")
st.pop()
st.pop()
st.pop()
print("The size of the stack is", st.size())
