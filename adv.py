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



# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

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
    
    def direction(self):
        return self.stack[-1]




# Fill this out with directions to walk
#traversal_path = ['n', 'n'] # line
# traversal_path = ['n', 'n', 's', 's', 's', 's', 'n', 'n', 'e', 'e', 'w', 'w', 'w', 'w']
# traversal_path = ['n','n','s','s','s','s', 'w', 'w', 'n', 'n', 'e', 'e', 'e', 'e']  # loop
# traversal_path = ['e', 'e', 'w', 'w', 'w', 'w', 's', 's', 'e', 'e', 'n', 'n', 'n', 'n', 's', 'e', 'e', 'n', 's', 'w', 'w', 'w', 'w', 'n'] # loop_fork
traversal_path = []

###########################################################################
# First Attempt:  Could not figure out how to implement BFS correctly

# def bfs(self, start, end):

#     q = Queue()
#     q.enqueue([start])
#     visited_rooms = set()


#     while q.size() > 0:
#         current_path= q.dequeue()
#         current_node = current_path[-1]

#         if current_node not in visited_rooms:
#             if current_node == end:
#                 return current_path
             
#             visited_rooms.add(current_node)

#             neighbors = self.get_neighbors(current_node)
#             for neighbor in neighbors:
#                 path_copy = current_path.copy()
#                 path_copy.append(neighbor)
#                 q.enqueue(neighbor)

#     return None




##################################################################################
# My Practice

# opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# print("STEP 1:")
# path = []
# print(path)
# # print("room_graph: ", room_graph)
# print(player.current_room.id)
# print(player.current_room.get_exits())

# print("STEP 2:")
# player.travel("n")
# print(player.current_room.id)
# print(player.current_room.get_exits())
# path.append("n")
# print(path)

# print("STEP 3:")
# player.travel("n")
# print(player.current_room.id)
# print(player.current_room.get_exits())
# path.append("n")
# print(path)

# print("STEP 4:")
# print(opposite["n"])
# path.append(opposite["n"])
# print(path)

# print("STEP 5:")
# direction = path[-1]
# print(direction)
# path.append(direction)
# print(path)
############################################################################


# Second Attempt: Did not use Stack or Queue classes

visited = {}                                            ## created a dictionary for visited
reverse = []                                            ## list of reverse traversal_path
opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}     ## set to define movement in the opposite direction

# print("STARTING ROOM: ", player.current_room)
visited[player.current_room.id] = player.current_room.get_exits()  ## sets initial room and defines exit directions 

while len(visited) < len(room_graph):                   ## Operations to perform while the visited rooms is less than total rooms in the graph
    if player.current_room.id not in visited:
        
        visited[player.current_room.id] = player.current_room.get_exits()  ## adds players current room to visited
        # print("player.current_room.get_exits(): ",player.current_room.get_exits())
        direction = reverse[-1]
        # print("direction room direction: ", direction)
        visited[player.current_room.id].remove(direction)
        # print("CURRENT ROOM: ", player.current_room)
       
    if len(visited[player.current_room.id]) > 0:            ## number of rooms not visited is greater than 0
        direction = visited[player.current_room.id][-1]     ## grab and assigns the first available exit direction for the room
        visited[player.current_room.id].pop()               ## pop the [0th] direction from the list
        traversal_path.append(direction)                    ## put the direction into traversal_path
        reverse.append(opposite[direction])                 ## put the opposite[direction] into reverse
        player.travel(direction)                            ## move the player in the direction
        # print("player.travel(direction): ", direction)  
    else:
        direction = reverse[-1]                              ## backup until an unvisited room is found (opposite direction)
        reverse.pop()                                        ## pop the [0th] direction from the list
        traversal_path.append(direction)                     ## put the opposite direction into traversal_path 
        player.travel(direction)                             ## move the player in the opposite direction


#####################################################################################

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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
##########################################################
