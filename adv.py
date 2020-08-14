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
map_file = "/Users/krishnadahal/Sprint-Challenge--Graphs/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Coding starts from here

class Stack:
    def __ini__(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size > 0:
            return self.stack.pop()
        else:
            return None

class MazeRunner:
    def __init__(self, starting_room): #initializing the props of class MazeRunner
        self.path = []
        self.direction_stack = Stack()
        self.visited = set()
        self.starting_room = starting_room
        self.player = Player(starting_room)
        self.current_room = self.starting_room

    def find_path(self):
        return self.path
    
    def move(self,direction):
        new_room = self.current_room.get_room_in_direction(direction)
        self.current_room = new_room
        player.travel(direction)
        self.path.append(direction)
    
    def make_path(self):
        exits = self.starting_room.get_exits()
        #goes through all exits possible at current roon
        for i in exits:
            self.direction_stack.push((i, "Forward"))
        #add as visited room
        self.visited.add(self.current_room)

        #check if all rooms are visited
        while self.direction_stack.size()>0:
            if len(self.visited) == len(world.rooms):
                return
            direction_info = self.direction_stack.pop()

            if direction_info[1] is "Forward": #if not visited room, we need to visit it
                if self.current_room.get_room_in_direction(direction_info[0]) not in self.visited:
                    self.move(direction_info[0])
                    #once visited, add it to visited list
                    self.visited.add(self.current_room)
                    self.add_directions(direction_info[0])
            elif direction_info[1] is "Back": #if already visited
                self.move(direction_info[0])
    
    def add_directions(self,last_direction):
        self.direction_stack.push((opposite(last_direction),"Back"))
        #finding available direction
        available_directions = self.current_room.get_exits()

        for ad in available_directions:
            room = self.current_room.get_room_in_direction(ad)
            if room not in self.visited:
                self.direction_stack.push((ad,"Forward"))
    
#if no direction available, move opposite
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
        return None

maze_Runner = MazeRunner(world.starting_room)
maze_Runner.make_path()
traversal_path = maze_Runner.find_path()

# Coding ends here


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
