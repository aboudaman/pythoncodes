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

    # Add script to search for item
    def search(self, item):
        current = self.head
        found = False
        while not current == None and found == False:
            if current.getData() ==  item:
                found = True
            else:
                current = current.getNext()
        return found

    # Add method to remove item
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    # Add method to append to the list
    def append(self, item):
        temp = Node(item)
        temp.getNext() = None
        current = self.head

        while not current.getNext() == None:
            temp = current
            current = current.getNext()
            
        if current.getNext() == None:






mylist = UnorderedList()
mylist.add(23)
mylist.add(22)
mylist.add(22)
mylist.add("Hola")
print(mylist.size())
# print(mylist.search(24))
print(mylist.remove(23))
