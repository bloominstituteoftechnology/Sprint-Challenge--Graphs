from room import Room
from player import Player
from world import World
from queue import Queue

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "Sprint-Challenge--Graphs/maps/test_line.txt"
# map_file = "Sprint-Challenge--Graphs/maps/test_cross.txt"
# map_file = "Sprint-Challenge--Graphs/maps/test_loop.txt"
# map_file = "Sprint-Challenge--Graphs/maps/test_loop_fork.txt"
map_file = "Sprint-Challenge--Graphs/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
unexplored = set() 

def bft(player):
    q = Queue()
    visited = set()
    q.enqueue([("s", player.current_room.id)]) # Enqueue the starting vertex with its direction

    while q.size() > 0:
        path = q.dequeue() 
        cur_room = path[-1] # last vertex from the path
        
        if player.current_room not in visited:
            visited.add(player.current_room.id)

        # Iterate through the exits
        for direction in world.rooms[cur_room[1]].get_exits():
            # Check if cur_rooms neighbor is in unexplored (global)
            if world.rooms[cur_room[1]].get_room_in_direction(direction) not in unexplored:
                # Add (room.id, direction)
                path.append((direction, world.rooms[cur_room[1]].get_room_in_direction(direction).id))
                print(path)
                return path
            # Check if cur_rooms neighbor.id is in visited (intern)
            if world.rooms[cur_room[1]].get_room_in_direction(direction).id not in visited:
                new_room = world.rooms[cur_room[1]].get_room_in_direction(direction)
                new_path = path.copy()       
                # Add room with direction & Id
                new_path.append((direction, new_room.id))
                visited.add(new_room.id)
                q.enqueue(new_path)

def move(path):
    # iterate through the range of path and get directions to append to traversal_path
    for i in range(1, len(path)):
        direction = path[i][0]
        player.travel(direction)
        traversal_path.append(direction) # test is using this!
    unexplored.add(player.current_room)
                
while(len(unexplored) != len(room_graph)):
    # find shortest path
    move(bft(player))


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
