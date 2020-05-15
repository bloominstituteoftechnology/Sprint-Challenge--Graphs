from room import Room
from player import Player
from world import World
from utils import Stack, Queue, Graph

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
#world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


#traversal_path = []

count = 0

def run_maze():
    visited = set()
    graph = Graph()
    travel_path = []
    dfs_rooms = graph.dfs(player.current_room)
    rooms = [room for room in dfs_rooms]
    while(len(visited) < len(room_graph) - 1):
        current_room = rooms[0]
        next_room = rooms[1]
        shortest_path = graph.bfs(current_room, next_room)

        while len(shortest_path) > 1:
            current_room_neighbors = dfs_rooms[shortest_path[0]]
            next_room = shortest_path[1]
            if next_room in current_room_neighbors:
                travel_path.append(current_room_neighbors[next_room])
            shortest_path.remove(shortest_path[0])
        rooms.remove(current_room)
        visited.add(current_room)

    return travel_path

traversal_path = []

def test_traversal(test_traversal_path):
    visited_rooms = set()
    testplayer = Player(world.starting_room)
    testplayer.current_room = world.starting_room
    visited_rooms.add(testplayer.current_room)

    for move in test_traversal_path:
        testplayer.travel(move)
        visited_rooms.add(testplayer.current_room)

    if len(visited_rooms) == len(room_graph):
        print(f"Tests Passed: {len(test_traversal_path)} moves {len(visited_rooms)} rooms visited")
    else:
        print("TEST FAILED: INCOMPLETE TRAVERSAL")
        print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

def get_low():
    global traversal_path
    traversal_path = run_maze()

    if len(traversal_path) < 960:
        print("Less than 960!")
        return
    
    prev_traversal = len(traversal_path)
    travel_count = 0
    while len(traversal_path) > 946:
        travel_count += 1
        if travel_count in range(0, 1000000000000000, 5000):
            print('running for', travel_count)
        traversal_path = run_maze()
        if len(traversal_path) < prev_traversal:
            print('Current lowest:', len(traversal_path), "at:", travel_count)
            prev_traversal = len(traversal_path)
            test_traversal(traversal_path)

    print('Total runs:', travel_count)

get_low()


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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
