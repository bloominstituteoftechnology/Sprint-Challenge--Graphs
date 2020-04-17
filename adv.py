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

def get_opposite_direction(direction):
    if direction == None:
        return None
    dirs = ["n", "e", "s", "w"]
    return dirs[(dirs.index(direction) + 2) % 4]

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

traversal_path = []


stack = [] # Keep a stack of previous moves
checked = {} # Keep checked directions
max_dist = {}
stack.append((player.current_room, None, None, 0))
while len(stack) > 0:
    node = stack[-1]
    room = node[0]
    last_dir = node[1]
    if room.id not in checked:
        checked[room.id] = set()
    if last_dir is not None:
        checked[room.id].add(last_dir)
    if len(checked) == len(room_graph):
        break
    exits = room.get_exits()
    exits_valid = [i for i in exits if i not in checked[room.id]]
    if len(exits_valid) > 0:
        direction = random.choice(exits_valid)
        room_to = room.get_room_in_direction(direction)
        checked[room.id].add(direction)
        stack.append((room_to, get_opposite_direction(direction)))
        traversal_path.append(direction)
    else:
        traversal_path.append(last_dir)
        stack.pop(-1)


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
