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
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
traversal_path = []

def dft(starting_vertex):
    s = Stack()
    visited = set()
    visit_order = []

    s.push(starting_vertex)

    while s.size() > 0:
        vert = s.pop()
        if vert not in visited:
            
            visited.add(vert)
            visit_order.append(vert)
            if vert.e_to != None:
                s.push(vert.e_to)
            if vert.s_to != None:
                s.push(vert.s_to)
            if vert.w_to != None:
                s.push(vert.w_to)
            if vert.n_to != None:
                s.push(vert.n_to)
            
            
            
            
            
            
            
            
            
            
    return visit_order
#print('check', dft(world.starting_room))
def bfs(starting_vertex, destination_vertex):
    q = Queue()
    visited = set()
    path_order = []
    q.enqueue([(starting_vertex, 'x')])

    while q.size() > 0:
        path = q.dequeue() 
            
        if path[-1] not in visited:
            visited.add(path[-1])
            
            if path[-1][0].e_to != None:
                if path[-1][0].e_to == destination_vertex:
                    path_order = path[:]
                    path_order.append((path[-1][0].e_to, 'e'))
                    return path_order
                new_path = path[:]
                new_path.append((path[-1][0].e_to, 'e'))
                q.enqueue(new_path)
            
            if path[-1][0].s_to != None:
                if path[-1][0].s_to == destination_vertex:
                    path_order = path[:]
                    path_order.append((path[-1][0].s_to, 's'))
                    return path_order
                new_path = path[:]
                new_path.append((path[-1][0].s_to, 's'))
                q.enqueue(new_path)

            if path[-1][0].w_to != None:
                if path[-1][0].w_to == destination_vertex:
                    path_order = path[:]
                    path_order.append((path[-1][0].w_to, 'w'))
                    return path_order
                new_path = path[:]
                new_path.append((path[-1][0].w_to, 'w'))
                q.enqueue(new_path)
            
            if path[-1][0].n_to != None:
                if path[-1][0].n_to == destination_vertex:
                    path_order = path[:]
                    path_order.append((path[-1][0].n_to, 'n'))
                    return path_order
                new_path = path[:]
                new_path.append((path[-1][0].n_to, 'n'))
                q.enqueue(new_path)

            
            
            

            
            
            
                
            
        
    return None
print('check2',bfs(world.starting_room, world.starting_room.n_to))
def build_route(starting_room):
    room_order = dft(starting_room)
    path_taken = []
    for i in range(len(room_order)-1):
        path_section = bfs(room_order[i], room_order[i+1])
        for x in path_section:
            if x[1] != 'x':
                path_taken.append(x[1])
    return path_taken
traversal_path = build_route(world.starting_room)
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
