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

# project code begins here

def check_room(room):
    """
    if a room hasn't been visited, adds it to explored rooms
    and returns True; if not, returns False.
    """
    if room not in rooms_explored:
        rooms_explored[room] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}

        exits = room.get_exits()

        for direction in rooms_explored[room]:
            if direction not in exits:
                rooms_explored[room][direction] = None

        return True
    else:
        return False

def connect_rooms(origin, direction, destination):
    """
    like add_friendship(), but for rooms. connects two rooms
    along a given direction.
    """
    rooms_explored[origin][direction] = destination
    rooms_explored[destination][inverter[direction]] = origin

def bfs_for_unexplored_rooms(origin):
    """
    breadth-first search for an unexplored room, then return
    the path to it.
    """

    visited = set() # rooms we've seen
    q = [] # rooms to check

    q.append((origin, [])) # empty list is the path to the room

    while len(q) > 0: # while there's still rooms to check
        (room, path) = q.pop(0) # get the top item in the queue and its path
        
        # if needed, add the room to visited
        if room in visited:
            continue
        else:
            visited.add(room)

        # take a look at all the directions for the current room
        for direction in rooms_explored[room]:
            if rooms_explored[room][direction] == '?':
                # if we find a '?' we'll return the path
                return path
            elif rooms_explored[room][direction] is not None:
                # otherwise, as long as the direction is valid:
                updated_path = path.copy() # copy the old path
                updated_path.append(direction) # add on the direction we moved in to get here
                next_room = rooms_explored[room][direction] # get the next room itself
                q.append((next_room, updated_path))

    return []

def do_traversal():

    check_room(player.current_room) # add current room to the dict

    while len(rooms_explored) < len(room_graph): # while we've not explored every room
        
        room = player.current_room # get current room
        exits = room.get_exits() # get exits

        unexplored_flag = False

        for direction in inverter: # for each direction
            if rooms_explored[room][direction] == '?' and direction in exits:
                # if the room is new and exists, flag it, go there, 
                # add it to path, update current room.
                unexplored_flag = True
                player.travel(direction)
                next_room = player.current_room
                traversal_path.append(direction)

                if check_room(next_room) == False: # if the next room isn't new
                    player.travel(inverter[direction]) # go back the other way
                    traversal_path.pop() # and remove that instruction

                connect_rooms(room, direction, next_room) # connect the rooms
                break

        if unexplored_flag == False: # if no unexplored rooms were found
            path = bfs_for_unexplored_rooms(room) # get a path to the closest unexplored room

            traversal_path.extend(path) # add the backtrack to the path
            for direction in path: # follow the path
                player.travel(direction)

rooms_explored = {} # our map
inverter = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
do_traversal()
                    

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



"""#######
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
        print("I did not understand that command.")"""
