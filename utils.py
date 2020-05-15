import random

count = 0

def rando_exit(length):
    rand = random.randrange(0, length)

    return rand

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

class Stack():
    def __init__(self):
        self.s = []
    def push(self, value):
        self.s.append(value)
    def pop(self):
        if self.size() > 0:
            return self.s.pop()
        else:
            return None
    def size(self):
        return len(self.s)

class Graph:
    def __init__(self):
        self.vertices = {}

    def dfs(self, starting_vertex):
        visited_rooms = set()
        s = Stack()
        s.push([starting_vertex])
        while s.size() > 0:
            current_room = s.pop()
            room = current_room[-1]
            if room not in visited_rooms:
                self.vertices[room.id] = {}
                exits = room.get_exits()
                for direction in exits:
                    next_room = room.get_room_in_direction(direction)
                    self.vertices[room.id][next_room.id] = direction
                visited_rooms.add(room)
                while len(exits) > 0:
                    rando = rando_exit(len(exits))
                    direction = exits[rando]
                    neighbors = list(current_room)
                    neighbors.append(room.get_room_in_direction(direction))
                    s.push(neighbors)
                    exits.remove(direction)
        return self.vertices

    def bfs_rooms(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        visited_rooms = set()

        while q.size() > 0:
            path = q.dequeue()
            room = path[-1]

            if room == destination_vertex:
                return path
            else:
                if room not in visited_rooms:
                    self.vertices[room.id] = {}
                    exits = room.get_exits()
                    for direction in exits:
                        next_room = room.get_room_in_direction(direction)
                        self.vertices[room.id][next_room.id] = direction
                    visited_rooms.add(room)
                    while len(exits) > 0:
                        direction = exits[0]
                        neighbors = list(path)
                        neighbors.append(room.get_room_in_direction(direction))
                        q.enqueue(neighbors)
                        exits.remove(direction)
        return self.vertices

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        visited_rooms = set()

        while q.size() > 0:
            path = q.dequeue()
            room = path[-1]
            if room == destination_vertex:
                return path

            else:
                if room not in visited_rooms:
                    visited_rooms.add(room)
                    edges = self.vertices[room]
                    for next_vert in edges:
                        path_copy = list(path)
                        path_copy.append(next_vert)
                        q.enqueue(path_copy)
