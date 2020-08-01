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
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_room(self, room):
        if room not in self.graph:
            self.graph[room] = set()
    
    def add_edge(self, room1, room2):
        self.graph[room1].add(room2)
    
    def get_neighbors(self, room):
        return self.graph[room]
    
    def size(self):
        return len(self.graph)



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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def bfs(self, start, end):

    q = Queue()
    q.enqueue([start])
    visited = set()


    while q.size() > 0:
        current_path= q.dequeue()
        current_node = current_path[-1]

        if current_node not in visited:
            if current_node == end:
                return current_path
             
            visited.add(current_node)

            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                path_copy = current_path.copy()
                path_copy.append(neighbor)
                q.enqueue(neighbor)

    return visited
#--------------------------------------------------
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
