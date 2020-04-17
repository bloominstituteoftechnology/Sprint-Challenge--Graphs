from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# queue is used for searching for exits: 
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# stack is for stacking the rooms together:
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
# because player moves in both drections n-s e-w  and room has two exits!
reversed_path = []

# You may find the commands `player.current_room.id`, - gettting ids of every room
# `player.current_room.get_exits()` - gets all possible exits
# and `player.travel(direction)` useful. - travels in that direction 


path = {} # dict for the rooms 
reverse = {'n' :'s', 's': 'n', 'e': 'w' ,'w' :'e'}
# where is the player , starting point 0
path[0] = player.current_room.get_exits()
complete_path = []
print(path[0])
print(len(path))

print(len(room_graph) -1)
print(len(room_graph))

# so go through all the rooms:
while len(path) < len(room_graph) -1:
    # get the players starting position and all the possible exits^^^:
    if player.current_room.id not in path:
        path[player.current_room.id] = player.current_room.get_exits()
        # check for rooms in reverse until all rooms are visited
        previous_room = reversed_path[-1]
        path[player.current_room.id].remove(previous_room)

    # finally after getting to the last room:
    while len(path[player.current_room.id]) < 1:
        # add all rooms to visited:
        visited = reversed_path.pop()
        # and append visited to the test path:
        traversal_path.append(visited)
        # have the player go through the copy of all rooms:
        player.travel(visited)

    # finally get all the exits and append them to the test path:
    exits = path[player.current_room.id].pop()
    traversal_path.append(exits)
    # also append the exits to reversed path 
    reversed_path.append(reverse[exits])
    # have the player travel through all the exits
    player.travel(exits)

# then get the triversed path
# and print all the possible paths from start to end
if len(traversal_path)<9999:
    for i in traversal_path:
        print(f"walk {i} to get to next room") 




# def bft(rooms, num_rooms):
#     # set traveled to
#     traveled = set()
#     traveled.add(rooms.id)
#     # find the exits
#     exits = rooms.get_exits()
#     # 
#     s = Stack()
#     # (build)stack all possible directions:
#     for e in exits:
#         s.push(rooms.get_room_in_direction(e))
#     # if there are rooms that havent been visited yet
#     while len(traveled) < num_rooms:
#         next_room = s.pop()
#         if next_room.id in traveled:
#             # continue because we need the exit to next room
#             continue
#         # now que (because we are searching) the exits:
#         q = Queue()
#         # now search for exit:
#         for e in exits:
#             q.enqueue([e])
    
#     # initialize visited
#         visited = set()
#     # search for the rooms with an exit:
#         while q.size() > 0: 
#             path = q.dequeue()
#             for e in path:
#                 rooms = rooms.get_room_in_direction(e)
#             new_exits = rooms.get_exits()
#             if rooms.id not in visited:
#                 visited.add(rooms.id)
#             # if you reach the destination room, stop
#                 if rooms == next_room:
#                     break
#                 for e in new_exits:
                
#                     def reverse(direction):
#                         if direction == 'w':
#                             return 'e'
#                         elif direction == 'e':
#                             return 'w'
#                         elif direction == 'n':
#                             return 's'
#                         else:
#                             return 'n'
#                     if e  == reverse(path[-1]):
#                         return
#                     new_path = list(path)
#                     new_path.append(e)
#                     q.enqueue(new_path)
    
#     for e in path:
#         rooms = rooms.get_room_in_direction(e)
#         complete_path.append(e)

#         # finally marked the next room traveled:
#         traveled.add(rooms.id)
#     exits = rooms.get_exits()

#     for e in exits:
#         final_room = rooms.get_room_in_direction(e)
#         if final_room.id not in traveled:
#             s.push(final_room)
        
#     return complete_path

# traversal_path = bft(world.starting_room, len(room_graph))

# while True:
#     if traversal_path < 980:
#         break
#     traversal_path = bft(world.starting_room, len(room_graph))


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


    # def get_all_social_paths(self, user_id):
    # # Note: This Queue class is sub-optimal. Why?
    #     """
    #     Takes a user's user_id as an argument

    #     Returns a dictionary containing every user in that user's
    #     extended network with the shortest friendship path between them.

    #     The key is the friend's ID and the value is the path.
    #     """
    #     visited = {}  # Note that this is a dictionary, not a set
    #     # !!!! IMPLEMENT ME
    #     for friend_id in self.users:
    #         connection = self.bfs(user_id, friend_id)
    #         if connection:
    #             visited[friend_id] = connection
    #     return visited

    # def bft_find_furthest(self, starting_vertex):
    #     qq= Queue()
    #     qq.enqueue(starting_vertex)
    #     visited = set()
    #     while qq.size() > 0:
    #         v = qq.dequeue()
    #         if v not in visited:
    #             visited.add(v)
    #             for n in self.get_neighbors(v):
    #                 qq.enqueue(n)
    #         if qq.size() == 0:
    #             # return furthest:
    #             if v == starting_vertex:
    #                 return -1 
    #             else:
    #                 return v
    