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

# Function to flip directions
def get_opposite_direction(direction):
    if direction == None:
        return None
    dirs = ["n", "e", "s", "w"]
    if direction in dirs:
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
stack.append((player.current_room, None)) # Push starting room with no past direction
while len(stack) > 0:
    node = stack[-1] # Get current room/direction
    room = node[0]
    last_dir = node[1]
    if room.id not in checked: # If new room, add to checked dict
        checked[room.id] = set()
    if last_dir is not None: # If moved from another room, set direction to checked
        checked[room.id].add(last_dir)
    if len(checked) == len(room_graph): # If all rooms, checked, break out
        break
    exits = room.get_exits() # Get valid exits (exits not taken yet)
    exits_valid = [i for i in exits if i not in checked[room.id]]
    if len(exits_valid) > 0:
        direction = random.choice(exits_valid) # Choose random direction
        traversal_path.append(direction) # Add to traversal path
        checked[room.id].add(direction) # Set direction to checked
        room_to = room.get_room_in_direction(direction) # Get next room
        stack.append((room_to, get_opposite_direction(direction))) # Push next room with opposite direction
    else: # If cannot find a valid path
        traversal_path.append(last_dir) # Keep popping from the stack and backtrack
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
