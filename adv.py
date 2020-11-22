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

def reverse(d):
    if d == "w":
        return "e"
    if d == "n":
        return "s"
    if d == "s":
        return "n"
    if d == "e":
        return "w"
    if d == None:
        return None
graph = {}


def explore(came_from=None):
    to_visit = Stack()

    if player.current_room.id not in graph:
        graph[player.current_room.id] = {}

    if came_from is not None:
        graph[player.current_room.id][reverse(
            came_from)] = player.current_room.get_room_in_direction(reverse(came_from)).id

    for direction in player.current_room.get_exits():
        if direction not in graph[player.current_room.id]:
            graph[player.current_room.id][direction] = '?'

    for direction in player.current_room.get_exits():
        adj_room = player.current_room.get_room_in_direction(direction).id

        if adj_room not in graph or graph[player.current_room.id][direction] == '?':
            to_visit.push(direction)

    while to_visit.size() > 0:

        go_to = to_visit.pop()

        if player.current_room.get_room_in_direction(go_to).id not in graph:
            traversal_path.append(go_to)
            graph[player.current_room.id][go_to] = player.current_room.get_room_in_direction(
                go_to).id
            player.travel(go_to)
            explore(go_to)

            if len(graph) == len(world.rooms):
                return

            traversal_path.append(reverse(go_to))
            player.travel(reverse(go_to))


print(explore())






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
