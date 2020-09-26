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
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

opposite_dir = { 'w': 'e', 'e': 'w', 'n': 's', 's': 'n' }

# dfs, backtrack, but will take long loop arounds. 1st iteration. 998 moves
def dfs(room, path, d, visited=set()):
    if room.name not in visited:
        if d:
            path.append(d)
        visited.add(room.name)
        for exit in room.get_exits():
            room_in_dir = room.get_room_in_direction(exit)
            if room_in_dir.name not in visited:
                dfs(room_in_dir, path, exit, visited)
                path.append(opposite_dir[exit])

dfs(player.current_room, traversal_path, "")

visited2 = {}
stack = [player.current_room]

# find a way to detect cycles and pop the rooms out of the stack until you're back

def check_cycle(curr_room, stack):
    for i in range(len(stack)-2, -1,-1):
        for exit in stack[i].get_exits():
            if stack[i].name not in visited2 or exit not in visited2[stack[i].name]:
                return -1
        if curr_room == stack[i]:
            return i
    return -1

def dfs2(path, stack):
    d = ""
    revisits = 0
    rooms = len(world.rooms)
    while stack and len(visited2) < rooms:
        curr_room = stack[-1]
        if curr_room.name in visited2: revisits += 1
        if curr_room.name not in visited2:
            visited2[curr_room.name] = set()
        if d:
            visited2[curr_room.name].add(opposite_dir[d])
        complete = True
        for exit in curr_room.get_exits():
            room_in_dir = curr_room.get_room_in_direction(exit)
            if room_in_dir.name not in visited2 or exit not in visited2[curr_room.name]:
                d = exit
                complete = False
                path.append(d)
                visited2[curr_room.name].add(d)
                stack.append(room_in_dir)
                break
        if complete:
            cycle = check_cycle(curr_room, stack)
            if cycle >= 0:
                stack = stack[:cycle]
            else:
                stack.pop()
            if not stack:
                return
            prev_room = stack[-1]
            x = curr_room.x - prev_room.x
            y = curr_room.y - prev_room.y
            if x < 0: path.append('e')
            if x > 0: path.append('w')
            if y < 0: path.append('n')
            if y > 0: path.append('s')
    print(revisits)
# dfs2(traversal_path, stack)

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
