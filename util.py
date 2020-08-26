class Queue:
    def __init__(self):
        self.store = []

    def size(self):
        return len(self.store)

    def enqueue(self, val):
        self.store.append(val)

    def dequeue(self):
        if self.size() > 0:
            return self.store.pop(0)
        else:
            return None


class Stack:
    def __init__(self):
        self.store = []

    def size(self):
        return len(self.store)

    def push(self, value):
        self.store.append(value)

    def pop(self):
        if self.size() > 0:
            return self.store.pop()
        else:
            return None
