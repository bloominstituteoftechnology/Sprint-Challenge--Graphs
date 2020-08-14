from room import Room
from player import Player
from world import World
import random
from ast import literal_eval

# Initialize world and player at room 000
world = World()
map_file = "maps/main_maze.txt"
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
player = Player(world.starting_room)

# ------------------------- Functions ----------------------------------

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

def directions(): return player.current_room.get_exits() 
def travel(direction): player.travel(direction)
def roomInfo(player): return player.current_room.print_room_description(player)
def roomCoords(): return player.current_room.get_coords()
def nextRoomInfo(direction): return player.current_room.get_room_in_direction(direction)
def reverseDirection(direction):
    if direction == 'n': return 's'
    elif direction == 's': return 'n'
    elif direction == 'e': return 'w'
    elif direction == 'w': return 'e'

# ----------------------- Traverse Maze --------------------------------

paths = Stack()
visited = set()
traversal_path = []
count = 0

while len(visited) < len(world.rooms):

    current = []
    for door in directions(): # Each possible direction
        if door is not None and nextRoomInfo(door) not in visited: 
            current.append(door)

    visited.add(player.current_room)

    if len(current) > 0: # Move in random direction
        move = random.randint(0, len(current) - 1) 
        paths.push(current[move])
        travel(current[move])
        traversal_path.append(current[move])
    else: # Dead end, go back
        end = paths.pop()
        travel(reverseDirection(end))
        traversal_path.append(reverseDirection(end))

# -------------------------------------------------------------------

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

