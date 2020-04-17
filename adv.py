from room import Room
from player import Player
from world import World
from util import Stack, Queue
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

# TRAVERSAL TEST
# visited_rooms = set()
visited = set() # set of all room IDs that we have visited in our traversal
player.current_room = world.starting_room
# visited_rooms.add(player.current_room)
visited.add(player.current_room)

#returns a shortest path to a room that has not been explored yet
def do_bst(current_room, total_traversed, world):
    qq = Queue()
    qq.enqueue([('n', current_room.id)])
    visited = set() #already seen by our bst
    visited.add(current_room.id)
    while qq.size() > 0:
        curr_path = qq.dequeue()
        curr_room_pair = curr_path[-1]
        curr_room = world.rooms[curr_room_pair[1]]

        for direction in curr_room.get_exits():
            if curr_room.get_room_in_direction(direction) not in total_traversed:
                curr_path.append((direction, curr_room.get_room_in_direction(direction).id))
                return curr_path
            elif curr_room.get_room_in_direction(direction).id not in visited:
                new_room = curr_room.get_room_in_direction(direction)
                new_path = curr_path.copy()
                new_path.append((direction, new_room.id))
                visited.add(new_room.id)
                qq.enqueue(new_path)        

#pick random unexplored area from current room
while(len(visited) != len(room_graph)):
    current_exits = player.current_room.get_exits()
    found_unexplored_exit = False
    for direction in current_exits:
        if player.current_room.get_room_in_direction(direction) not in visited:            
            player.travel(direction)
            visited.add(player.current_room)
            traversal_path.append(direction)
            found_unexplored_exit = True
            break
    if found_unexplored_exit:
        continue
    #all adjacent rooms were visited, need to perform BST to find shortest path
    path = do_bst(player.current_room, visited, world)
    for i in range(1, len(path)):
        dir = path[i][0]
        player.travel(dir)
        traversal_path.append(dir)
    visited.add(player.current_room)

if len(visited) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited)} unvisited rooms")



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
