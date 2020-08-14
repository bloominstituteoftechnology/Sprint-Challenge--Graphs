from room import Room
from player import Player
from world import World

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

#Create a dictionary for visited rooms
visited = {}
#Set the room player is in to 'visited'

visited[player.current_room.id] = True

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#Create list of rooms to visit
rooms_to_visit = []

def traverse():
    found_exit = True  #create 'found_exit variable, set to 'true'.
    while found_exit:
        found_exit = False
        exits = player.current_room.get_exits()  #use room get exits function
        # go to first unexplored (?) direction or the direction that ends in an exit
        current = player.current_room
        possible_rooms = []  #create list of possible rooms
       #look for rooms - if not visited add to possible rooms
        for direction in exits:
            if current.get_room_in_direction(direction).id not in visited:
                possible_rooms.append((current.get_room_in_direction(direction), direction))
        

        if len(possible_rooms) > 0:
            room_to_traverse = possible_rooms[0]
            for i in range(len(possible_rooms)):
                # if one room ends in an exit, take it
                if len(possible_rooms[i][0].get_exits()) < 2:
                    room_to_traverse = possible_rooms[i]
                    

            # add other rooms to rooms_to_visit
            for room in possible_rooms:
                if room != room_to_traverse:
                    rooms_to_visit.append(room[0].id)
            room, direction = room_to_traverse
            player.travel(direction)
            traversal_path.append(direction)
            visited[room.id] = True
            found_exit = True
        # loop until no unexplored direction

def find_shortest_path_to_unexplored(dest):
    #Create containers for visited rooms and queues
    visited_room = set()

    q = Queue()
    q2 = Queue()

    q.enqueue([])
    q2.enqueue(player.current_room)
    destination = dest

    while q.size() > 0:
        path = q.dequeue()
        current = q2.dequeue()
        if current.id not in visited_room:
            visited_room.add(current.id)
            if current.id == destination:
                return path
            exits = current.get_exits()
            for direction in exits:
                path_copy = list(path)
                path_copy.append(direction)
                q.enqueue(path_copy)
                q2.enqueue(current.get_room_in_direction(direction))
    return None

def find_unexplored(path):
    # Send player on their way
    for direction in path:
        player.travel(direction)
        traversal_path.append(direction)
    visited[player.current_room.id] = True

while len(world.rooms) > len(visited):
    traverse()
    if len(visited) != len(world.rooms):
        # Find the closest of the unexplored rooms
        paths = []
        for unvisited in rooms_to_visit:
            paths.append(find_shortest_path_to_unexplored(unvisited))
        # iterate through all the paths to the remaining unvisited rooms
        shortest_path = None
        first_iter = True
        for path in paths:
            if first_iter:
                shortest_path = path
                first_iter = False
                
            if len(path) <= len(shortest_path):
                shortest_path = path
        # travel to the closest one
        find_unexplored(shortest_path)
        # remove that room from rooms_to_visit
        rooms_to_visit.remove(player.current_room.id)

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
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#          player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#          break
#     else:
#          print("I did not understand that command.")
