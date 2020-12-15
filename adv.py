# from room import Room
# from player import Player
# from world import World

# import random
# from collections import deque
# from ast import literal_eval

# # Load world
# world = World()

# class Queue:
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

# # You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# # map_file = "maps/test_cross.txt"
# # map_file = "maps/test_loop.txt"
# # map_file = "maps/test_loop_fork.txt"
# # map_file = "maps/main_maze.txt"

# # Loads the map into a dictionary
# room_graph=literal_eval(open(map_file, "r").read())
# world.load_graph(room_graph)
# mapDictionary = {}

# # Print an ASCII map
# world.print_rooms()

# player = Player(world.starting_room)

# # Fill this out with directions to walk
# # traversal_path = ['n', 'n']
# traversal_path = []
# # opposite_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# # Pick a random unexplored direction from current room, travel and log that direction, then loop. When reach dead end, walk back and find nearest room that is unexplored.

# # def traversal(starting_room=player.current_room):
# #     exits = player.current_room.get_exits()
# #     current_room = player.current_room.id

# #     visited = set()
# #     stack = deque()
# #     stack.append([starting_room])

# #     for direction in exits:
# #         if current_room in visited:
# #             print(visited)

# # def traverse_map(starting_room, visited=[]):
# #     path = []

# #     for direction in player.current_room.get_exits():
# #         player.travel(direction)
# #         if player.current_room.id in visited:
# #             player.travel(opposite_directions[direction])
# #         else:
# #             visited.append(player.current_room.id)
# #             path.append(direction)
# #             path = path + traverse_map(player.current_room.id, visited)
# #             player.travel(opposite_directions[direction])
# #             path.append(opposite_directions[direction])

# #     return path


# # traversal_path = traverse_map(player.current_room.id)

# # Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order.

# # def bfs(self, starting_room):
# #     visited_rooms = set()
# #     queue = Queue()
# #     queue.enqueue([starting_room])

# #     while queue.size() > 0:
# #         currPath = queue.dequeue()
# #         currNode = currPath[-1]
# #         visited_rooms.add(currNode)

# #         for direction in mapDictionary[currNode]: 
# #             if mapDictionary[currNode][direction] == "?":
# #                 return currPath
# #             if mapDictionary[currNode][direction] not in visited_rooms:
# #                 newPath = list(currPath)
# #                 newPath.append(mapDictionary[currNode][direction])
# #                 queue.enqueue(newPath)

# def bfs(starting_room):
#     visited_rooms = set()
#     queue = Queue()
#     queue.enqueue([starting_room])
#     while queue.size() > 0:
#         currPath = queue.dequeue()
#         currNode = currPath[-1]
#         visited_rooms.add(currNode)
#         for direction in mapDictionary[currNode]:
#             if mapDictionary[currNode][direction] == "?":
#                 return currPath
#             if mapDictionary[currNode][direction] not in visited_rooms:
#                 newPath = list(currPath)
#                 newPath.append(mapDictionary[currNode][direction])
#                 queue.enqueue(newPath)

# # using dft to create the maze
# # def dft(starting_room):
# #     # reverse the directions
# #     reverse_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# #     # create counter for rooms the player has been to
# #     # visited = set()
# #     # stack = deque()
# #     # stack.append([starting_room])
# #     # exits = player.current_room.get_exits()
# #     visited = 0
    
# #     # while the len of mapDictionary is not equal to the len of the graph...
# #     while len(mapDictionary) is not len(room_graph):
# #         # see the room currently in
# #         current_room = player.current_room
# #         # find the room id of the current room
# #         room_id = current_room.id
# #         # create a dict for the rooms
# #         visited_rooms = {}

# #         # check if the room id is not in the mapDictionary...
# #         if room_id not in mapDictionary:
# #             # then find the possible exits
# #             for i in current_room.get_exits():
# #                 # add the '?' into the visited_rooms
# #                 visited_rooms[i] = '?'
# #             # update the room
# #             if traversal_path:
# #                 # find the previous room
# #                 prev_room = reverse_directions[traversal_path[-1]]
# #                 # add the previous room to the room counter and the visited_rooms
# #                 visited_rooms[prev_room] = visited
# #             # add the unexplored rooms to the room id
# #             mapDictionary[room_id]= visited_rooms
# #         # otherwise...
# #         else:
# #             # add the room id from mapDictionary to the inner room dict
# #             visited_rooms = mapDictionary[room_id]
# #         # create an empyt list of possible exits
# #         possible_exits = list()
# #         # iterate throuogh the room dict
# #         for i in visited_rooms:
# #             # check if '?' is at the index direction...
# #             if visited_rooms[i] == '?':
# #                 # if so, add the direction to the possible exits list
# #                 possible_exits.append(i)
# #         # check if there is an unknown direction...
# #         if len(possible_exits) != 0:
# #             # use random and shuffle the possible exits
# #             random.shuffle(possible_exits)
# #             # set the direction to the zero index of possible exits
# #             direction = possible_exits[0]
# #             # add the direction to the traversal path
# #             traversal_path.append(direction)
# #             # to move the player in that direction, use travel function
# #             player.travel(direction)
# #             # Grab player's current room
# #             player_room = current_room
# #             # set mapDictionary current room id and direction to player room id
# #             mapDictionary[current_room.id][direction] = player_room.id
# #             # now set the current room id to the counter
# #             visited = current_room.id
# #         # otherwise...
# #         else:
# #             # going to use bfs to search for next exit or possible rooms
# #             next_room = bfs(room_id)
# #             # check if the path of the next room is not None and if len of next room not None...
# #             if next_room != None and len(next_room) > 0:
# #                 # find index in the range of the len on the next room - 1 (not include current room)...
# #                 for i in range(len(next_room) - 1):
# #                     # find direction in mapDictionary of index of next room
# #                     for direction in mapDictionary[next_room[i]]:
# #                         # check if the mapDictionary's index of next room and direction is equal to the index + 1 of next room
# #                         if mapDictionary[next_room[i]][direction] is next_room[i + 1]:
# #                             # if so, then add the direction to traversal path
# #                             traversal_path.append(direction)
# #                             # then move the player to that room
# #                             player.travel(direction)
# #             # otherwise, break
# #             else:
# #                 break



# # TRAVERSAL TEST - DO NOT MODIFY
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# # player.current_room.print_room_description(player)
# # while True:
# #     cmds = input("-> ").lower().split(" ")
# #     if cmds[0] in ["n", "s", "e", "w"]:
# #         player.travel(cmds[0], True)
# #     elif cmds[0] == "q":
# #         break
# #     else:
# #         print("I did not understand that command.")

import random
from ast import literal_eval

from player import Player
from room import Room
# from util import Queue, Stack
from world import World


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


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Notes from README:
# Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal.
# You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` for an exit. If you use the `bfs` code from the homework, you will need to make a few modifications.
# 1. Instead of searching for a target vertex, you are searching for an exit with a `'?'` as the value. If an exit has been explored, you can put it in your BFS queue like normal.
# 2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Graph as a dict
mapDictionary = {}


# trying with bfs to search for shortest path
# def bfs(starting_room_id):
#     # Create an empty queue
#     q = Queue()
#     # Add a path to the starting room to the queue
#     q.enqueue([starting_room_id])
#     # Create an empty set to store visited
#     visited = set()
#     # While the queue is not empty...
#     while q.size() > 0:
#         # Dequeue the first path
#         path = q.dequeue()
#         # Grab the last room from the path
#         current_room = path[-1]
#         # add current_room to visited
#         visited.add(current_room)
#         # For each direction in the map graph's current room...
#         for direction in mapDictionary[current_room]:
#             # check if the current room's direction is a '?'...
#             if mapDictionary[current_room][direction] is '?':
#                 # if it is, return path
#                 return path
#             # check else if the current room's direction is not visited...
#             if mapDictionary[current_room][direction] not in visited:
#                 # if not, create a new path, add the direction
#                 new_path = list(path)
#                 new_path.append(mapDictionary[current_room][direction])
#                 q.enqueue(new_path)


# # using dft to create the maze
# def dft(starting_room):
#     # reverse the directions
#     reverse_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
#     # create counter for rooms the player has been to
#     counter = 0
#     # while the len of mapDictionary is not equal to the len of the graph...
#     while len(mapDictionary) is not len(room_graph):
#         # see the room currently in
#         current_room = player.current_room
#         # find the room id of the current room
#         room_id = current_room.id
#         # create a dict for the rooms
#         room_dict = {}
#         # check if the room id is not in the mapDictionary...
#         if room_id not in mapDictionary:
#             # then find the possible exits
#             for i in current_room.get_exits():
#                 # add the '?' into the room_dict
#                 room_dict[i] = '?'
#             # update the room
#             if traversal_path:
#                 # find the previous room
#                 prevRoom = reverse_directions[traversal_path[-1]]
#                 # add the previous room to the room counter and the room_dict
#                 room_dict[prevRoom] = counter
#             # add the unexplored rooms to the room id
#             mapDictionary[room_id] = room_dict
#         # otherwise...
#         else:
#             # add the room id from mapDictionary to the inner room dict
#             room_dict = mapDictionary[room_id]
#         # create an empyt list of possible exits
#         possible_exits = list()
#         # iterate throuogh the room dict
#         for direction in room_dict:
#             # check if '?' is at the index direction...
#             if room_dict[direction] is '?':
#                 # if so, add the direction to the possible exits list
#                 possible_exits.append(direction)
#         # check if there is an unknown direction...
#         if len(possible_exits) is not 0:
#             # use random and shuffle the possible exits
#             random.shuffle(possible_exits)
#             # set the direction to the zero index of possible exits
#             direction = possible_exits[0]
#             # add the direction to the traversal path
#             traversal_path.append(direction)
#             # to move the player in that direction, use travel function
#             player.travel(direction)
#             # Grab player's current room
#             player_room = player.current_room
#             # set mapDictionary current room id and direction to player room id
#             mapDictionary[current_room.id][direction] = player_room.id
#             # now set the current room id to the counter
#             counter = current_room.id
#         # otherwise...
#         else:
#             # going to use bfs to search for next exit or possible rooms
#             next_room = bfs(room_id)
#             # check if the path of the next room is not None and if len of next room not None...
#             if next_room is not None and len(next_room) > 0:
#                 # find index in the range of the len on the next room - 1 (not include current room)...
#                 for i in range(len(next_room) - 1):
#                     # find direction in mapDictionary of index of next room
#                     for direction in mapDictionary[next_room[i]]:
#                         # check if the mapDictionary's index of next room and direction is equal to the index + 1 of next room
#                         if mapDictionary[next_room[i]][direction] is next_room[i + 1]:
#                             # if so, then add the direction to traversal path
#                             traversal_path.append(direction)
#                             # then move the player to that room
#                             player.travel(direction)
#             # otherwise, break
#             else:
#                 break

##############################################

def bfs(starting_room):
    visited_rooms = set()
    queue = Queue()
    queue.enqueue([starting_room])
    while queue.size() > 0:
        currPath = queue.dequeue()
        currNode = currPath[-1]
        visited_rooms.add(currNode)
        for direction in mapDictionary[currNode]:
            if mapDictionary[currNode][direction] == "?":
                return currPath
            if mapDictionary[currNode][direction] not in visited_rooms:
                newPath = list(currPath)
                newPath.append(mapDictionary[currNode][direction])
                queue.enqueue(newPath)


def dft(starting_room):
    # reverse the directions
    reverse_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    # create counter for rooms the player has been to
    # visited = set()
    # stack = deque()
    # stack.append([starting_room])
    # exits = player.current_room.get_exits()
    visited = 0
    # while the len of mapDictionary is not equal to the len of the graph...
    while len(mapDictionary) is not len(room_graph):
        # see the room currently in
        current_room = player.current_room
        # find the room id of the current room
        room_id = current_room.id
        # create a dict for the rooms
        visited_rooms = {}
        # check if the room id is not in the mapDictionary...
        if room_id not in mapDictionary:
            # then find the possible exits
            for i in current_room.get_exits():
                # add the '?' into the visited_rooms
                visited_rooms[i] = '?'
            # update the room
            if traversal_path:
                # find the previous room
                prev_room = reverse_directions[traversal_path[-1]]
                # add the previous room to the room counter and the visited_rooms
                visited_rooms[prev_room] = visited
            # add the unexplored rooms to the room id
            mapDictionary[room_id] = visited_rooms
        # otherwise...
        else:
            # add the room id from mapDictionary to the inner room dict
            visited_rooms = mapDictionary[room_id]
        # create an empyt list of possible exits
        possible_exits = list()
        # iterate throuogh the room dict
        for i in visited_rooms:
            # check if '?' is at the index direction...
            if visited_rooms[i] == '?':
                # if so, add the direction to the possible exits list
                possible_exits.append(i)
        # check if there is an unknown direction...
        if len(possible_exits) != 0:
            # use random and shuffle the possible exits
            random.shuffle(possible_exits)
            # set the direction to the zero index of possible exits
            direction = possible_exits[0]
            # add the direction to the traversal path
            traversal_path.append(direction)
            # to move the player in that direction, use travel function
            player.travel(direction)
            # Grab player's current room
            player_room = current_room
            # set mapDictionary current room id and direction to player room id
            mapDictionary[current_room.id][direction] = player_room.id
            # now set the current room id to the counter
            visited = current_room.id
        # otherwise...
        else:
            # going to use bfs to search for next exit or possible rooms
            next_room = bfs(room_id)
            # check if the path of the next room is not None and if len of next room not None...
            if next_room != None and len(next_room) > 0:
                # find index in the range of the len on the next room - 1 (not include current room)...
                for i in range(len(next_room) - 1):
                    # find direction in mapDictionary of index of next room
                    for direction in mapDictionary[next_room[i]]:
                        # check if the mapDictionary's index of next room and direction is equal to the index + 1 of next room
                        if mapDictionary[next_room[i]][direction] is next_room[i + 1]:
                            # if so, then add the direction to traversal path
                            traversal_path.append(direction)
                            # then move the player to that room
                            player.travel(direction)
            # otherwise, break
            else:
                break


#####################################


# call dft room_graph, otherwise get INCOMPLETE TRAVERSAL error
dft(room_graph)
print("----")
print(f"MAP DICTIONARY: {mapDictionary}")
print("----")
print(f"TRAVERSAL PATH: {traversal_path}")
print("----")


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    print("----")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    print("----")


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