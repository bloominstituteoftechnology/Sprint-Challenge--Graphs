from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# Use player.current_room.id, player.current_room.get_exits() and player.travel(direction)

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

def dft(starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    s = Stack()
    s.push(starting_vertex)

    # Keep track of visited nodes
    visited = set()

    # Keep track of rooms visited order
    visited_order = []

    # Repeat until stack is empty
    while s.size() > 0:
        # Pop last vert
        v = s.pop()

    # If it's not visited:
        if v not in visited:
            # print(v)

        # Mark visited
            visited.add(v)
            # print(visited)
            visited_order.append(v)
            # for next_vert in self.get_neighbors(v):
            #     s.push(next_vert)
            if v.n_to is not None:
                s.push(v.n_to)
            if v.s_to is not None:
                s.push(v.s_to)
            if v.e_to is not None:
                s.push(v.e_to)
            if v.w_to is not None:
                s.push(v.w_to)
    return visited_order

def bfs(starting_vertex, target_vertex):
    q = Queue()
    visited = set()
    q.enqueue([(starting_vertex, 'start')])

    while q.size() > 0:
        path = q.dequeue()

        if path[-1] not in visited:
            visited.add(path[-1])

            if path[-1][0].n_to is not None:
                if path[-1][0].n_to == target_vertex:
                    path_order = path[:]
                    path_order.append((path[-1][0].n_to, 'n'))
                    return path_order
                new_path = path[:]
                new_path.append((path[-1][0].n_to, 'n'))
                q.enqueue(new_path)
            if path[-1][0].s_to is not None:
                if path[-1][0].s_to == target_vertex:
                    path_order = path[:]
                    path_order.append((path[-1][0].s_to, 's'))
                    return path_order
                new_path = path[:]
                new_path.append((path[-1][0].s_to, 's'))
                q.enqueue(new_path)
            if path[-1][0].e_to is not None:
                if path[-1][0].e_to == target_vertex:
                    path_order = path[:]
                    path_order.append((path[-1][0].e_to, 'e'))
                    return path_order
                new_path = path[:]
                new_path.append((path[-1][0].e_to, 'e'))
                q.enqueue(new_path)
            if path[-1][0].w_to is not None:
                if path[-1][0].w_to == target_vertex:
                    path_order = path[:]
                    path_order.append((path[-1][0].w_to, 'w'))
                    return path_order
                new_path = path[:]
                new_path.append((path[-1][0].w_to, 'w'))
                q.enqueue(new_path)

    pass


print('check2', bfs(world.starting_room, world.starting_room.n_to))

def pathing(starting_room):
    rooms = dft(starting_room)
    path = []
    for i in range(len(rooms) - 1):
        path_part = bfs(rooms[i], rooms[i+1])
        for j in path_part:
            if j[1] != 'start':
                path.append(j[1])
    return path


traversal_path = pathing(world.starting_room)






# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
