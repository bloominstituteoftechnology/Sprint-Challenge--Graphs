from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# IMPORTS
from utils import Queue, Stack
import random

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

# -- START CODE -- #
# -- START CODE -- #

#### #### #### #### #### #### #### #### 
##          Sunday Clean Up          ##
#### #### #### #### #### #### #### ####

# - A - SETUP
reverse_direction = {'n':'s', 'e':'w', 's':'n', 'w':'e'}
visited_rooms = {}

# - B - HELPERS
def unused_exits(visited_rooms, current_room):
    result = []
    available_exit_directions = current_room.get_exits()
    print(f'-*- AVAILABLE EXIT DIRECTIONS: {available_exit_directions}')

    for direction in available_exit_directions:
        if current_room.get_room_in_direction(direction).id not in visited_rooms:
            result.append(direction)

    if len(result) == 0:
        return False
    else:
        return result

def random_direction(filtered_moves):
    return filtered_moves[
        random.randint(0, len(filtered_moves) - 1)
    ]

def backtrack(visited_rooms, current_room):
    queue_of_PATHS = Queue()

    available_backtrack_directions = current_room.get_exits()
    print(f'-*- AVAILABLE BACKTRACK EXIT DIRECTIONS: {available_backtrack_directions}')

    for direction in available_backtrack_directions:
        queue_of_PATHS.enqueue(direction)
    print(f'-*- CURRENT QUEUE OF PATHS: {queue_of_PATHS.print_queue()}')

    while queue_of_PATHS.size() > 0 and len(visited_rooms) < len(world.rooms):
        path = queue_of_PATHS.dequeue()
        print(f'-*- CURRENT PATH: {path}')

        player.current_room = current_room
        print(f'LOOOOOOOOOOOOOK: -*- PLAYER CURRENT ROOM: {player.current_room}')
        # print(f'LOOOOOOOOOOOOOK: -*- PLAYER CURRENT ROOM: {player.current_room}')

        for move in path:
            player.travel(move)
            # print(player.current_room)
        print(f'-*- CURRENT TEST ROOM: {player.current_room}')
        
        filtered_backtrack_moves = unused_exits(visited_rooms, player.current_room)
        print(f'-*- FILTERED BACKTRACK MOVES FROM CURRENT TEST ROOM: {filtered_backtrack_moves}')

        if filtered_backtrack_moves is not False:
            print('-!- Return Path')
            print(f'-*- SHORTEST PATH: {path}')
            return path

        else: 
            print('-!- ADD ALL NEW PATH OPTIONS')

            for direction in player.current_room.get_exits():
                print(direction)
                DUPLICATE_path = list(path)
                DUPLICATE_path.append(direction)
                queue_of_PATHS.enqueue(DUPLICATE_path)
            print(f'-*- CURRENT QUEUE OF PATHS: {queue_of_PATHS.print_queue()}')
    
    return [] # NO UNUSED EXITS --> ALGO FINISHED :) 
    # exit()








    # q = Queue()
    # q.enqueue(current_room)
    # #?? Known Distances?
    # # array the length of all the nodes 
    # # for room world.rooms:
    #     # known_distance = [-1 for i in world.rooms ]
    # backtrack_traversal_path = []

    # while q.size() > 0:
    #     current_room = q.dequeue()
    #     available_backtrack_directions = current_room.get_exits()
    #     print(f'-*- AVAILABLE BACKTRACK EXIT DIRECTIONS: {available_backtrack_directions}')
    #     # print(f'------ TEST ROOM IN THAT DIRECTION ------')


    #     for direction in available_backtrack_directions:
    #         q.enqueue(current_room.get_room_in_direction(direction))

    #     test_room = q.dequeue()
    #     print(f'------ DEQUEUED TEST ROOM ------ : {test_room}')
    #     # test_direction = q.dequeue()
        
    #     filtered_moves = unused_exits(
    #         visited_rooms,
    #         test_room
    #         # current_room.get_room_in_direction(test_direction)
    #     )
    #     print(f'-*- FILTERED MOVES: {filtered_moves}')

    #     if filtered_moves is not False:
    #         print('-!- STOP BACKTRACKING')
    #         break

    #     else:
    #         print('-!- CONTINUE BACKTRACKING')
            

 
# - C - STEPS
s = Stack()
s.push(player.current_room)
print(f'-*- PLAYER CURRENT ROOM: {player.current_room}')

while len(visited_rooms) < len(world.rooms):
    current_room = s.pop()
    print(f'-*- CURRENT ROOM: {current_room}')

    if current_room.id not in visited_rooms:
        visited_rooms[current_room.id] = {}

    available_exits = current_room.get_exits()
    for direction in available_exits:
        connected_room = current_room.get_room_in_direction(direction)
        visited_rooms[current_room.id][direction] = connected_room.id
    print(f'-*- VISITED ROOMS: {visited_rooms}')
    print(f'-*- # VISITED ROOMS vs # ROOM IN WORLD: {len(visited_rooms)} / {len(world.rooms)}')

    if len(visited_rooms) == len(world.rooms):
        break
    

    filtered_moves = unused_exits(visited_rooms, current_room)
    print(f'-*- FILTERED MOVES: {filtered_moves}')
    if filtered_moves is not False:
        print('-!- CONTINUE w/ DFS')

        chosen_direction = random_direction(filtered_moves)
        print(f'-*- CHOSEN DIRECTOIN: {chosen_direction}')
        traversal_path.append(chosen_direction)
        print(f'-*- TRAVERSAL PATH: {traversal_path}')

        player.travel(chosen_direction)
        s.push(player.current_room)

    else: 
        print('-!- BACKTRACK w/ BFS')
        result = backtrack(visited_rooms, current_room)
        print(f'BACKTRACK RESULT: {result}')

        for direction in result:
            traversal_path.append(direction)
        print(f'-*- UPDATED TRAVERSAL PATH w/ BACKTRACK RESULT: {traversal_path}')

        print(f'-*- PLAYER CURRENT ROOM: {player.current_room}')

        # for move in traversal_path:
        #     player.travel(move)
        #     print(player.current_room)

        # current_room = player.current_room
        s.push(player.current_room)

# exit()





# # while s.size() > 0:
# while len(visited_rooms) < len(world.rooms):
#     curr_room = s.pop()
#     print(f'-*- CURRENT ROOM: {curr_room}')

#     visited_rooms[curr_room.id] = {}

#     available_exits = curr_room.get_exits()
#     print(f'-*- AVAILABLE EXITS: {available_exits}')
#     filtered_exit_options = []
#     for direction in available_exits:
#         next_room_option = curr_room.get_room_in_direction(direction)
#         print(f'-*- NEXT ROOM OPTION: {next_room_option}')
        
#         # visited_rooms[curr_room.id][direction] = '?'
#         visited_rooms[curr_room.id][direction] = next_room_option.id
        
#         if next_room_option.id not in visited_rooms:
#             filtered_exit_options.append(direction)
#             print(f'-*- FILTERED AVAILABLE EXITS: {filtered_exit_options}')
    
#     print(f'-*- VISITED ROOMS: {visited_rooms}')
#     print(f'-*- LENGTH VISITED ROOMS: {len(visited_rooms)}')
#     print(f'-*- LENGTH WORLD ROOMS: {len(world.rooms)}')

#     if len(filtered_exit_options) == 0 and len(visited_rooms) < len(world.rooms):
#         print('NEED TO BACKTRACK')
#         #  FIND SHORTEST PATH BACK TO A ROOM WITH VALID EXIT OPTIONS
#         i = -1
#         keep_backtracking = True

#         # V2 -- USE TRAVERSAL PATH
#         while keep_backtracking:

#             backtrack_direction = reverse_direction[traversal_path[i]]
#             print(f'-*- BACKTRACK DIRECTION: {backtrack_direction}')

#             traversal_path.append(backtrack_direction)
#             print(f'-*- TRAVERSAL PATH: {traversal_path}')

#             player.travel(backtrack_direction)
#             print(player.current_room)

#             for direction in player.current_room.get_exits():
#                 print(direction)

#                 if player.current_room.get_room_in_direction(direction).id not in visited_rooms:
#                     print(f'STAY IN THIS ROOM')
#                     keep_backtracking = False
#                     break
#                 else:
#                     print(f'ALREADY EXPLORED')
#             i -= 1

#         s.push(player.current_room)
            
#         # exit()

#         # V1 -- USE A QUEUE
#         # q = Queue()

#         # for exit_option in available_exits:
#         #     q.enqueue(exit_option)
        
#         # back_track_room = q.dequeue()
#         # print(back_track_room)


#         # exit()
#     elif len(visited_rooms) < len(world.rooms): 
    
#         # Pick Movement Direction
#         chosen_direction = filtered_exit_options[
#             random.randint(0, len(filtered_exit_options) -1 )
#         ]
#         print(f'-*- CHOSEN DIRECTOIN: {chosen_direction}')

#         # Update Travesal Path
#         traversal_path.append(chosen_direction)
#         print(f'-*- TRAVERSAL PATH: {traversal_path}')

#         # Move Player
#         player.travel(chosen_direction)
#         s.push(player.current_room)

#     # else: 
#     #     print('ERROR')
#     #     exit()


    

# -- END CODE -- #
# -- END CODE -- #


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
