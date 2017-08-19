from node import Node

class UnorderedList:

# Create the Head for the list
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # Adding to the UnorderedList
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # Adding script to calculate size of the linked list
    def size(self):
        current = self.head
        count = 0
        # Start traversal
        while not current == None:
            count = count + 1
            current = current.getNext()
        return count

mylist = UnorderedList()
mylist.add(23)
mylist.add(22)
mylist.add(22)
print(mylist.size())
