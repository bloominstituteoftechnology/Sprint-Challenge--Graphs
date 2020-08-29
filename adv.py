from room import Room
from player import Player
from world import World

from utils import Queue, Stack, Graph

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

# print(f'%%%  room_graph[0]  {room_graph[0]} ')
# print(f'\t  room_graph[0][-1]  {room_graph[0][-1]}   ')

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# create graph 
g = Graph()
g.build_graph(room_graph)
print(f' g rooms >>  {g.rooms}')
# g rooms >>  {0: {'n': '?'}, 1: {'s': '?', 'n': '?'}, 2: {'s': '?'}}


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


print(f' current info {player.current_room} ')
print(f' current info id  {player.current_room.id} ')
print(f' exits:  {player.current_room.get_exits()}')



for room in g.rooms:
    print(f'  room: {room} >>  {g.rooms[room]}  ')


# set of visited rooms 
visited = set()


# TEST starting room 0
# room:0   g_room_dir {'n': '?', 's': '?', 'e': '?', 'w': '?'}

# MOVE 'n'
# player.travel('n')
# room:1   g_room_dir {'s': '?', 'n': '?'}       list_room_dir ['?', '?'] 

def bfs_path(current_room_id):
    
    
    q = Queue()                     # Create a queue
    q.enqueue([current_room_id])    # enqueue path to starting room
    visited_rooms = set()           # Create a set to store visited for backtrack

    
    # While the queue is NOT empty:
    while q.size() > 0:

    
        path = q.dequeue()                  # Dequeue the first PATH 
        print(f' dequeued path is : {path}')
        room_now = path[-1]                 # get room at end of path
        print(f' room_now is {room_now} ')

        g_room_dir_vals = g.rooms[room_now].values()
        g_room_dir_v_list = list(g_room_dir_vals)
        print(f'>>>>>>> BFS >> g_room_dir_v_list {g_room_dir_v_list} ')


        if room_now not in visited_rooms:
            # add last if NOT in visited_room
            visited_rooms.add(room_now)
            
            #  queue new paths 
            for room in g_room_dir_vals:    
                print(f' \t\t g_room_dir_vals   {g_room_dir_vals}')
                print(f' ^^^^^^^^^^ room  {room}')
                new_p = path[:]
                new_p.append(room)
                print(f'   new_p NOW  {new_p} ')
                q.enqueue(new_p)
            print(f' \t\t  NOW equeued paths {q.queue}')

        # does g.rooms still have ? values
        if  '?'  in g_room_dir_v_list:    
            # not done, keep building path to get back to starting room

            print(f'\t\t\t BFS DONE  with g_room_dir_v_list  {g_room_dir_v_list} at room {room_now}')
            return path




exits_taken = 0

def get_avail_directions():
    # track unexplored available directions
    avail_dir = []

    for exits in player.current_room.get_exits():
        # print(f' >>> player.current_room.id  {player.current_room.id}    exits: {exits}')
        # print(f' \t g >>room: {g.rooms[player.current_room.id]} >>> g.rooms[player.current_room.id][exits] : {g.rooms[player.current_room.id][exits]}    actual_exits: {exits}')

        # Find known directions NOT travelled yet
        if g.rooms[player.current_room.id][exits] == '?':
            print(f' \t current_room:  {player.current_room.id}    exits avail: {exits}')
            avail_dir.append(exits)
            global exits_taken
            exits_taken += 1

    print(f' \t\t\t avail_dir choices: {avail_dir}')
    return random.choice(avail_dir)

# TEST
# get_avail_directions()


while len(visited) < len(room_graph):
    
    # !!!!!   3
    g_room_dict = g.rooms[player.current_room.id]
    g_room_dict_vals_list = list(g_room_dict.values())

    print(f' room:{player.current_room.id}   g_room_dir {g_room_dict}       list_room_dir {g_room_dict_vals_list} ')
    

    if  '?'  in g_room_dict_vals_list:
        print(f' Not Done')
        
        # RESET current room
        current_r = player.current_room.id 
        print(f' at TOP:  current room  >>>>>>> {current_r}')
        
        # find a known direction
        valid_exit = get_avail_directions()

        print(f' valid_exit  {valid_exit}')

        # find valid direction that has ? to path
        player.travel(valid_exit)
        print(f' \t\t\t\t\t\t   HEY, just walk into room  {player.current_room.id}')

        # track exits for TEST
        traversal_path.append(valid_exit)   # Nice   7 unvisited rooms

        # Check if current NOT yet visited
        if current_r not in visited:
            visited.add(current_r)
            print(f' \t\t visited NOW {visited}')

        # prepare backtrack directions update
        back_dir = {
        "n": "s",
        "s": "n",
        "e": "w",
        "w": "e"
        }        

        # get backtrack direction   
        back_direction = back_dir[valid_exit]

        # add to current room the previous direction just came from
        print(f' back_direction   {back_direction}')
        # print(f' g.rooms[player.current_room.id]  {g.rooms[player.current_room.id]} ')
        g.rooms[player.current_room.id][back_direction] = current_r

        print(f'  \t\t\t  Just came from room  >>> {g.rooms[player.current_room.id][back_direction]}  ')


        # attach info from current room to previous room info in g 
        print(f' $$ BEFORE g.rooms.current_r   {g.rooms[current_r]}') # {'n': '?', 's': '?', 'e': '?', 'w': '?'}
        g.rooms[current_r][valid_exit] = player.current_room.id 
        print(f' \t\t\t   We just entered room >>   {g.rooms[current_r][valid_exit]}')
        print(f' $$$$ AFTER g.rooms[current_r] {g.rooms[current_r]} ') # {'n': '?', 's': '?', 'e': '?', 'w': 7}

        # !!!!!!!!    apppend room in g to visited if not in visited
        if g.rooms[current_r][valid_exit] not in visited:
            visited.add(g.rooms[current_r][valid_exit])
        print(f' \t\t visited UPDATED {visited}')
        
        # update current g.rooms that direction came from (opposite) is also valid_exit
        print(f' ### g.rooms[player.current_room.id]  {g.rooms[player.current_room.id]}')
        # working on
        
    else:
        # backtrack and find other rooms
        backtrack_path = bfs_path(player.current_room.id)
        print(f' \t\t *>*>*> backtrack_path  {backtrack_path}') 
        break









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

print(f' exits_taken  {exits_taken}')

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
