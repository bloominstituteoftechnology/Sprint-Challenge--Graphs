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
room_graph = literal_eval(open(map_file, "r").read())
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


traversal_path = []


def reverse_direction(direction):
    if(direction == 'n'):
        return_direction = 's'

    if(direction == 's'):
        return_direction = 'n'

    if(direction == 'w'):
        return_direction = 'e'

    if(direction == 'e'):
        return_direction = 'w'

    return return_direction


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

moves_made = Stack()

while len(visited_rooms) < len(world.rooms):
    available_exits = player.current_room.get_exits()
    available_directions = [exit for exit in available_exits if player.current_room.get_room_in_direction(
        exit) not in visited_rooms]

    # add current room to visited set()
    visited_rooms.add(player.current_room)

    if len(available_directions):
        # pick a random direction and push it to the stack[]
        randomDirection = random.randint(0, len(available_directions) - 1)
        moves_made.push(available_directions[randomDirection])
        # move the player in chosen direction and append move to traversal_path[]
        player.travel(available_directions[randomDirection])
        traversal_path.append(available_directions[randomDirection])
    else:
        # if there are no available directions, get the latest move made
        latestMove = moves_made.pop()
        # reverse the last move and append to traversal_path[]
        player.travel(reverse_direction(latestMove))
        traversal_path.append(reverse_direction(latestMove))

[player.travel(move) and visited_rooms.add(player.current_room)
 for move in traversal_path]

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(
#         f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


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
