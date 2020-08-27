class Queue():   # FIFO   or LILO
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)      # REMEBER periodic resizing
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)    # this is O(n)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():      # LIFO
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)        # REMEBER periodic resizing
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()     # this is O(n)
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        self.rooms = {}

    def build_world(self, room_graph):
        for room in room_graph:
            if room not in self.rooms:
                self.rooms[room] = set()
