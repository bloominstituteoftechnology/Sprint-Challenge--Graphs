from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()







# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


# def dft_recursive(matrix,node,visited):
#     if node not in visited:
#         visited.add(node)
#     neighbors=getNeighbors(matrix,node)
#     for neighbor in neighbors:
#         dft_recursive(matrix)

# traversal_path = []
# visited={}
# discovered=[]
# breadcrumbs=[]



# at the current node in the adjancencyarray there are neighbors listed
# 
# base case is map[nextnode] is not None or Empty or Null
# 
# if map[nextnode] is empty or None or Null
#   return #
# #
# #
# def CheckNeighbors():
#     neighbors_list=matrix_list[currentnode.index][1]
#     if neighbors_list not None:
#         [discovered.append(neighbor) for neighbor in neighbors_list]

# def findNeighbors(map_adjancency_array,node):
# # start at entrynode 
#     current_room_data=map_adjancency_array[node.index]
#     traversal_path.append(node.index)

#     visited[node.index]=current_room_data
#     breadcrumbs.append(node.index)
#     new_neighbors= current_room_data[1]
#     # there is a new neighbor in this room
#     if new_neighbors is not None:
#         for neighbor in new_neighbors:
#             discovered.append(neighbor)
#         next_room = discovered[-1]
#         findNeighbors(map_adjancency_array, next_room)
#      # there is a no new neighbor in this room turn around
#     # there are unvisited neighbors in the discovered array
#     elif len(discovered) is not None:
#         last_visited=discovered[-1]
#         last_breadcrumb=breadcrumbs[-1]
#         if last_breadcrumb==last_visited:
#             breadcrumbs.pop()
#             visited.pop()
#             next_node=breadcrumbs[-1]
#         else:
#             next_node=visited.pop()
#         discovered.pop(-1)
#         traversal_path.append(check_visited)
#         if check_visited in visited:
#             check_visited=discovered[-1]
#     # there are no unvisited neighbors in the discovered array
#     else:
#         return traversal_path
           
# def check_visited(node):
#     next_node=discovered[-1]
#     discovered.pop()
#     traversal_path.append(next_node)
#     if next_node not in visited:
#         visited.append(next_node)


            







# #the entire path ['n','n','e','w','n','n','w','s','n','e','n'....]
# traversal_path=[]

# #directionwe just came from
# backtrack={"n":"s","s":"n","e":"w","w":"e"}

# #path we are currently exploring
# cur_path_tracker= []

# #current_room.id:current_room.get_exits()
# visited={}
# visited[player.current_room.id]= player.current_room.get_exits()

# def get_neighbors():
#     return player.current_room.get_exits()

# def dft(starting_vertex,visited=set()):
#     path=[]
    
#     if starting_vertex in visited:
#         return
    
#     else:
#         visited.add(starting_vertex)
#         path.append(starting_vertex)
#         neighbors= get_neighbors()
        
#         if len(neighbors)==0:
#             return None
        
#         for neighbor in get_neighbors():
#             dft(neighbor,visited)
    
#     return path
    
print("neighbors=>",get_neighbors())
print("dft(play.current_room.id)",dft(player.current_room.id))
    



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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
