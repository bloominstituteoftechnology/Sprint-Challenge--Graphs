from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


q = []
visited = {}


def add_to_visited():
    for exit in player.current_room.get_exits():
        if visited.get(player.current_room.id):
            visited[player.current_room.id][exit] = '?'
        else:
            visited[player.current_room.id] = {exit: '?'}


def add_path_to_prev(v, prev_id, cur_id):
    if v == 'n':
        visited[cur_id]['s'] = prev_id

    if v == 's':
        visited[cur_id]['n'] = prev_id

    if v == 'w':
        visited[cur_id]['e'] = prev_id

    if v == 'e':
        visited[cur_id]['w'] = prev_id


def reverse(v):
    if v == 'n':
        return 's'

    if v == 's':
        return 'n'

    if v == 'w':
        return 'e'

    if v == 'e':
        return 'w'


prev_id = player.current_room.id
add_to_visited()

traversal_path = []
backtrack = []

q.append(random.choice(player.current_room.get_exits()))
while len(q) > 0:
    v = q.pop()
    player.travel(v)
    backtrack.append(reverse(v))
    if prev_id is not player.current_room.id:
        add_to_visited()

    if visited[player.current_room.id].get(v) == '?':
        visited[prev_id][v] = player.current_room.id
        add_path_to_prev(v, prev_id, player.current_room.id)
    else:

        print('this ran')
        player.travel(backtrack[-1])
        backtrack.pop()

        for next_v in visited[player.current_room.id]:
            if visited[player.current_room.id][next_v] == '?':
                q.append(next_v)

    prev_id = player.current_room.id
    traversal_path.append(v)

    print(backtrack)
print(visited, player.current_room.id)
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    print(traversal_path)


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
