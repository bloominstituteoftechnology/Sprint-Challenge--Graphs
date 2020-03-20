from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
# print(room_graph)
world.load_graph(room_graph)


    

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print()
# traversal_path = [direction_stack]

# if 'n' in player.current_room.get_exits():
#     print("true")
# else: 
#     print("this isn't working")

# def world_traversal(self, player, room_graph): 

# print('this is what player looks like', player)

def world_traversal(self, player):
    direction_queue = Queue()
    visited = set()
    # starting_room = player
    direction_queue.enqueue( player )

    while direction_queue.size() < 499: 
        r = direction_queue.dequeue()
        if r not in visited:
            print(r)
            visited.add(r)
        for exits in self.player.get_exits(r):
            direction_queue.enqueue(exits)
        
    return world_traversal




    











#     if 'n' in player.current_room.get_exits(): 
#         # player.travel("n")
#         # visited.add(player.current_room)
#         direction_stack.push('n')
#         player.travel('n')
#         visited.add(player.current_room)
#         # print('n' in direction_stack)
#         print("stack inside of while loop", direction_stack.size())
#         print(len(visited))
#     elif 'n' not in player.current_room.get_exits():
#         pass

            

# print("this is the direction stack",direction_stack)


traversal_path = [i for i in direction_queue] 


            

# print('All possible exits', player.current_room.get_exits())
        

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# traversal_path = []



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

# print("should be seeing something here")



world_traversal(player=world.starting_room)
