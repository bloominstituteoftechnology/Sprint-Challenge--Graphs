from room import Room
from player import Player
from world import World

import random
from collections import deque
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
map_dict = {}

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = ['n', 's', 'w', 'e']
opposite_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# Pick a random unexplored direction from current room, travel and log that direction, then loop. When reach dead end, walk back and find nearest room that is unexplored.

# def traversal(starting_room=player.current_room):
#     exits = player.current_room.get_exits()
#     currRoom = player.current_room.id

#     visited = set()
#     stack = deque()
#     stack.append([starting_room])

#     for direction in exits:
#         if currRoom in visited:
#             print(visited)

# Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order.

def bfs(self, starting_room, destination_vertex = "?"):
    visited_rooms = set()
    queue = deque()
    queue.append ([starting_room])

    while len(queue) > 0:
        currPath = queue.popleft()
        currNode = currPath[-1]
        visited_rooms.add(currNode)

        for direction in map_dict[currNode]: 
            if currNode == "?":
                return currPath
            if currNode not in visited_rooms:
                for neighbor in self.visited_rooms:
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    queue.append(newPath)
    return []

# using dft to create the maze
def dft(starting_room):
    # reverse the directions
    reverse_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    # create counter for rooms the player has been to
    # while the len of mapDictionary is not equal to the len of the graph...
        # see the room currently in
        # find the room id of the current room
        # create a dict for the rooms
        # check if the room id is not in the mapDictionary...
            # then find the possible exits
                # add the '?' into the room_dict
            # update the room
            if traversal_path:
                # find the previous room
                # add the previous room to the room counter and the room_dict
            # add the unexplored rooms to the room id
        # otherwise...
            # add the room id from mapDictionary to the inner room dict
        # create an empyt list of possible exits
        # iterate throuogh the room dict
            # check if '?' is at the index direction...
                # if so, add the direction to the possible exits list
        # check if there is an unknown direction...
            # use random and shuffle the possible exits
            # set the direction to the zero index of possible exits
            # add the direction to the traversal path
            # to move the player in that direction, use travel function
            # Grab player's current room
            # set mapDictionary current room id and direction to player room id
            # now set the current room id to the counter
        # otherwise...
        else:
            # going to use bfs to search for next exit or possible rooms
            # check if the path of the next room is not None and if len of next room not None...
                # find index in the range of the len on the next room - 1 (not include current room)...
                    # find direction in mapDictionary of index of next room
                        # check if the mapDictionary's index of next room and direction is equal to the index + 1 of next room
                            # if so, then add the direction to traversal path
                            # then move the player to that room
            # otherwise, break

# def traverse_map(starting_room, visited=[]):
#     path = []

#     for direction in player.current_room.get_exits():
#         player.travel(direction)
#         if player.current_room.id in visited:
#             player.travel(opposite_directions[direction])
#         else:
#             visited.append(player.current_room.id)
#             path.append(direction)
#             path = path + traverse_map(player.current_room.id, visited)
#             player.travel(opposite_directions[direction])
#             path.append(opposite_directions[direction])

#     return path


# traversal_path = traverse_map(player.current_room.id)

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
