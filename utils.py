class Queue:
    """docstring for Queue Algorithm"""

    # declare array
    def __init__(self):
        self.queue = []

    # adding item
    def enqueue(self, value):
        self.enqueue.append(value)

    # removing item
    def dequeue(self, value):
        if self.value > 0:
            return self.queue.pop(0)
        else:
            return None

    # Get size of data
    def size(self):
        return len(self.queue)


class Stack:
    """docstring for Stack."""

    # Declare stack
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    # Removing Item
    def pop(self, value):
        if self.value > 0:
            self.stack.pop()
        else:
            return None
