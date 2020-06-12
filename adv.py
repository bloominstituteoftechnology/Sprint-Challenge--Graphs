from room import Room
from player import Player
from world import World
import random
from ast import literal_eval
from typing import List

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
# instantiate a player 
player = Player(world.starting_room)

""" UPER 
Use the room and player APIs to traverse the entire maze
Have to construct the graph as we walk around in the
form:
{ 
room_id : {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}

Player methods:
player.travel(direction key) to travel to valid room
player.current_room.id to get the current room's id

Room get methods methods:
exits with room.get_exits()
coordinates with room.get_coords()
the name of a next room with room.get_room_in_direction(direction)

So then we start in room zero like this:
Room_0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}

And we add this to the list of explored rooms:

explored_rooms: List[Room] = []

Also we need the return list of directions:

directions: List[str] = []

We start by checking exits with room.get_exits() and updating the ?s to 
which rooms they link to with get_room_in_direction(direction) . . . this is
too much work/confusing maybe do later if bored

Also checking that we haven't been there already with something like:

room.get_room_in_direction(direction) in explored_rooms == False

and then we go into a random valid next room and repeating this until we can
no longer do this and are at a dead end.

SAVE THE DIRECTIONS WE WENT IN ORDER SO CAN REVERSE WHEN WE REACH A DEAD END, I guess we can do this and the room together
and use whatever is the opposite of zip to seperate into a list of room sequences and direction sequences later

Then we back out until we can go to a new room.

So something like:

initialize traversal_path, rooms graph, starting room

DFT standard boiler plate code using a stack

stack.push(starting room, NONE)
graph = {}

while stack.size > 0:
    curr = s.PEEK() otherwise it is unable to reverse since it'll have done 2 pops and only 1 push
    add room to graph, add direction to list
    if curr not in graph:
        graph add curr
    if we moved somewhere:
        add direction to traversal_path
    if len(graph) == len(room_graph)
        break

    if able to go somewhere NEW, depth first search in random direction
        adding to graph and traversal_path
    else reverse until can go somewhere new
        adding to traversal_path
        pop where we were
    then when this else ends we go back up to the start of the while and DFS again 

  """
# copy paste from utils from graphs 
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
    def peek(self):
        return self.stack[-1]

# dictionary to hold inverse directions for backing up part         
reverse_directions = {'n':'s', 's':'n', 'w':'e', 'e':'w'}

def traverse_graph():
    traversal_path = []        
    s = Stack() # hold rooms and direction tuples that got us there so can reverse
    visited_graph = {} # holds k,v pairs of rooms and directions we've gone so far
    s.push(value=(player.current_room, None))
    while s.size() > 0:
        curr = s.peek()
        room, direction_traveled = curr[0], curr[1] 
        if room.id not in visited_graph: 
            visited_graph[room.id] = set() # initial set of directions we've gone, use set to avoid duplicates
        if direction_traveled: 
            visited_graph[room.id].add(direction_traveled) 
        # break if we visit all the rooms
        if len(visited_graph) == len(room_graph):
            break
        # DFS
        unexplored_branches = [direction for direction in room.get_exits() if direction not in visited_graph[room.id]]
        if unexplored_branches: # while there is somewhere to go, update everything
            random_direction = random.choice(unexplored_branches)
            print("CAN GO SOMEWHERE",random_direction)
            visited_graph[room.id].add(random_direction)         # update graph
            # push the room we go to and what direction to reverse if dead end   
            s.push(value=(room.get_room_in_direction(random_direction), reverse_directions[random_direction]))
            traversal_path.append(random_direction) 
        # backing up
        else: 
            print("BACKING UP", direction_traveled)
            traversal_path.append(direction_traveled)
            s.pop()
    return traversal_path

traversal_path = traverse_graph()

 
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    print("CURRENT ROOM", player.current_room)
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
