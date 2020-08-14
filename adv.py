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

traversal_path = []

opposite_path = {
    'n': 's',
    'e': 'w',
    's': 'n',
    'w': 'e',
}

# init graph
graph = {}

# Init Stack
class Stack():
    def __init__(self):
        self.stack = []

    # Add to Stack
    def push(self, value):
        self.stack.append(value)

    # Remove from stack
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

    # Return Stack size
    def size(self):
        return len(self.stack)

# Int Queue 
class Queue():
    def __init__(self):
        self.queue = []

    # Remove from queue
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)

    # Add to queue
    def enqueue(self, value):
        self.queue.append(value)
       
    # Length of queue
    def size(self):
        return len(self.queue)

def bfs(graph, starting_room):
    # Init queue
    q = Queue()
    # Store visited rooms
    visited = set()
    # Start path adding first vert to queue
    q.enqueue([starting_room])
    # If vert(s) in queue
    while q.size():
        # Remove first vert
        route = q.dequeue()
        # Get last vert added to path
        vertex = route[-1]
        # If vert unvisited, not in  set()
        if vertex not in visited:
            # Mark vert visited, add to set()
            visited.add(vertex)
            # Look for unvisited adjacent verts
            for vert in graph[vertex]:
                # print(vert)
                # If unvisited verts found
                if graph[vertex][vert] == '?':
                    # print(graph[vertex])
                    # Return route
                    return route

            for adjacent_verts in graph[vertex]:
                # Store adjacent verts
                surrounding_verts = graph[vertex][adjacent_verts]
                # !! New route 
                new_route = list(route)
                # Add adjacent vert to new route
                new_route.append(surrounding_verts)
                # Enqueue route
                q.enqueue(new_route)



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

# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
