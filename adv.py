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
