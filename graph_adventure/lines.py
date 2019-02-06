class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []

    def nq(self, value):
        self.queue.append(value)

    def dq(self):
        if self.size() > 0:
            return self.queue.pop()
        else:
            return None

    def size(self):
        return len(self.queue)
