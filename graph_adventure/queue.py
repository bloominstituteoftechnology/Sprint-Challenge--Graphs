class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        
    def size(self):
        return len(self.queue)

if __name__ == "__main__":

    q = Queue()
    q.enqueue(5)
    q.enqueue(23)
    q.enqueue(67)
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
