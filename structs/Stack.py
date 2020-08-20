# import sys
# sys.path.append('../doubly_linked_list')
from LinkedList import LinkedList

class Stack:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = LinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_from_tail()

    def len(self):
        return len(self.storage)

    def size(self):
        return len(self.storage)
