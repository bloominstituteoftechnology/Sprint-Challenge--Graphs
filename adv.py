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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

class PathBuilder:
    def __init__(self, starting_room):
        self.path = []
        self.direction_stack = Stack()
        self.visited = set()
        self.starting_room = starting_room
        self.player = Player(starting_room)
        self.current_room = self.starting_room

    def get_path(self):
        return self.path

    def move(self, direction):
        new_room = self.current_room.get_room_in_direction(direction)
        self.current_room = new_room
        player.travel(direction)
        self.path.append(direction)

    def build_path(self):
        exits = self.starting_room.get_exits()
        
        # Loop through the exits
        for i in exits:
            self.direction_stack.push((i, "Forward"))
        self.visited.add(self.current_room)

        # While the stack isn't empty
        while self.direction_stack.size() > 0:
            # Is the rooms visited is equal to the amount of total rooms
            if len(self.visited) == len(world.rooms):
                # we can return out
                return
            # We'll pop the direction off the direction stack
            direction_info = self.direction_stack.pop()

            if direction_info[1] is "Forward":
                # If the room hasn't been visited yet
                if self.current_room.get_room_in_direction(direction_info[0]) not in self.visited:
                    # We move in that direction
                    self.move(direction_info[0])
                    # add the current room to our set
                    self.visited.add(self.current_room)
                    # add the direction
                    self.add_directions(direction_info[0])
            elif direction_info[1] is "Back":
                self.move(direction_info[0])

    def add_directions(self, last_direction):
        # Push previous direction using our opposite function
        self.direction_stack.push((opposite(last_direction), "Back"))
        # The available direction would be whichever exits are available to us in the current room we're in
        available_directions = self.current_room.get_exits()

        # We'll loop through our available directions
        for available_direction in available_directions:
            room = self.current_room.get_room_in_direction(available_direction)
            # If the room has not been visited
            if room not in self.visited:
                # We can push the direction to the stack
                self.direction_stack.push((available_direction, "Forward"))

# If they can't move in a certain direction, provide the available directions
def opposite(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"
    else:
        # if they didn't select any of these options, do nothing
        return None

path_builder = PathBuilder(world.starting_room)
path_builder.build_path()
traversal_path = path_builder.get_path()

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