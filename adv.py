from room import Room
from player import Player
from world import World
from queue import Queue

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


def get_traversal_path():
    rooms = {}

    # modified DFT
    def dft(current_room, visited=None):
        if not visited:
            visited = set()
        elif current_room.id in visited:
            return

        visited.add(current_room.id)
        rooms[current_room.id] = {}
        exits = current_room.get_exits()

        for direction in exits:
            neighbor = current_room.get_room_in_direction(direction)
            rooms[current_room.id][direction] = neighbor.id
            dft(neighbor, visited)


    # modified BFS
    def bfs(starting_id, destination_id):
        q = Queue()
        q.put([starting_id])
        visited = set()

        while not q.empty():
            path = q.get()
            current_room_id = path[-1]

            if current_room_id in visited:
                continue

            if current_room_id == destination_id:
                return path
            visited.add(current_room_id)

            for room_id in rooms[current_room_id].values():
                q.put(path + [room_id])
    
    # traverse graph and fill rooms with directions
    # and ids of rooms in those directions
    dft(player.current_room)
    # grab ids of the rooms
    ids = list(rooms.keys())

    traversal_path = []

    # starts at first id and with every iteration moves up one
    for i in range(len(ids) - 1):
        # find path from first id to next
        path = bfs(ids[i], ids[i + 1])

        # iterate through path and append every direction to traversal path
        for j in range(len(path) - 1):
            cur_room_id, next_room_id = path[j], path[j + 1]
            for direction, room_id in rooms[cur_room_id].items():
                if room_id == next_room_id:
                    traversal_path.append(direction)

    return traversal_path

traversal_path = get_traversal_path()

# TRAVERSAL TEST
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
