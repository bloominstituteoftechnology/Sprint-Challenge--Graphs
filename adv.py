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


def cardinal_inverse(direction):
    if direction == 'n':
        return 's'
    if direction == 'e':
        return 'w'
    if direction == 's':
        return 'n'
    if direction == 'w':
        return 'e'


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graph = {}
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.
graph[player.current_room.id] = {
    'n': '?', 's': '?', 'w': '?', 'e': '?'}
# Fill this out while traversing
way_back = []
while len(visited_rooms) < len(room_graph):
    last_room = player.current_room.id

    print("current graph:", graph)

    exits_list = player.current_room.get_exits()
    print("current_room_id:", player.current_room.id)
    last_room = player.current_room.id
    q = []
    # loop over dictionary entry for current room, since visited rooms will be True, anything else will be False. That way rooms we don't need to visit can be kept ?
    for direction in exits_list:
        counter = 0
        if graph[player.current_room.id][direction] != True:
            graph[player.current_room.id][direction] = False
            counter += 1

    # check to see if it's a dead end
    if counter > 0:
        # make your way back to last not dead end
        while len(way_back) > 0:
            next_move = way_back.pop()
            player.travel(next_move)

    # if the dictionary value for the current room is false, add that direction to the q
    for direction in graph[player.current_room.id]:
        if graph[player.current_room.id][direction] == False:
            q.append(direction)
    # to keep it in line with BFT, pop the way to move off the end
    way_to_move = q.pop()
    print('Way to move:', way_to_move)
    # move in the direction
    player.travel(way_to_move)
    # add room to graph if not there already
    if player.current_room.id not in graph:
        graph[player.current_room.id] = {
            'n': '?', 's': '?', 'w': '?', 'e': '?'}
    # append the inverse cardinal direction to the way_back list
    way_back.append(cardinal_inverse(way_to_move))
    # add room to visited rooms
    visited_rooms.add(player.current_room)
    # add path to traversed list
    traversal_path.append(way_to_move)
    # update dictionary entries on both ends
    print('dict entry:', graph[last_room][way_to_move])
    graph[last_room][way_to_move] = True
    graph[player.current_room.id][cardinal_inverse(way_to_move)] = True


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


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
