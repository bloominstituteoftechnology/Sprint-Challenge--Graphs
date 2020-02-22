# 1 - Stack
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
    
    def print_stack(self):
        result = []
        for item in self.stack:
            result.append(item)
        return result

# 2 - Queue
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else: 
            return None
    
    def size(self):
        return len(self.queue)

    def print_queue(self):
        result = []
        for item in self.queue:
            result.append(item)
        return result


