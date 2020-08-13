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
traversal_path = []
backtrack = []
q.append(random.choice(player.current_room.get_exits()))
while len(q) > 0:
    current_room = player.current_room.id
    v = q.pop(0)

    backtrack.append(v)
    print(player.current_room.get_exits(), v, "exits, choice")

    if visited.get(current_room) is not None:

        if v not in visited.get(current_room):
            visited[current_room].add(v)
            for path in player.current_room.get_exits():
                q.append(path)
                break
        else:

            if player.current_room.get_exits == visited[current_room]:

                player.travel(backtrack[-1])
                backtrack.pop()

    elif visited.get(current_room) is None:
        visited[current_room] = set(v)

        for path in player.current_room.get_exits():
            q.append(path)
            break

    player.travel(v)
    backtrack.insert(0, v)
    traversal_path.append(v)

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
