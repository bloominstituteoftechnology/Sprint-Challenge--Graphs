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

    
    def build_graph(self, room_graph):
        # add each room to graph
        for room in room_graph:
            if room not in self.rooms:
                self.rooms[room] = set()

        # add direction info to each room
        for room in room_graph:
            for direction in room_graph[room][-1]:
                # print(f' dir {direction}')
                self.rooms[room] = room_graph[room][-1]
                room_info = self.rooms[room]
                dir_info = self.rooms[room][direction]
                # print(f' room: {room} self.room[room] >> {room_info}  self.rooms[room][direction] {dir_info}')    

                # ONLY for avail direction, change to '?'
                self.rooms[room][direction] = '?'