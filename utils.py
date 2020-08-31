class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None


    def size(self):
        return len(self.queue)
    
       

class Stack():

    def __init__(self,):
        self.stack = []


    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.size > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)
    