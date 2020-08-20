# import sys
# sys.path.append('../doubly_linked_list')
from LinkedList import LinkedList


class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        # cuz O(1) operation to add and remove from ends
        self.storage = LinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        return self.storage.remove_from_tail()

    def len(self):
        return len(self.storage)

    def size(self):
        return len(self.storage)
