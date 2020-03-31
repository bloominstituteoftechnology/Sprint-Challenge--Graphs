from room import Room
from player import Player
from world import World
# from util import Queue, Stack

import random
from ast import literal_eval

#Decided to code the queue and stack in here...  

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


# in order to get back to primary location reverse has been implemented...
def reverse(direction): 
    if direction == 'n':
        return 's'
    elif direction == 's': 
        return 'n'
    elif direction == 'e':
        return 'w'
    else: 
        return 'e'

def enter_room(room, visited_rooms):
    visited_rooms[room.id] = {}
    for exit_direction in room.get_exits():
        visited_rooms[room.id][exit_direction] = '?'

def bfs(visited_rooms): 
    visited = set()
    q = Queue()
    room = player.current_room

    #add room id
    q.enqueue([room.id])
    #while loop setup
    while q.size() > 0: 
        path = q.dequeue()
        #the last node
        end = path[-1]
        if end not in visited: 
            visited.add(end)
            #for loop that checks if last room has been visited
            for exit_direction in visited_rooms[end]: 
                #if no exit exists
                if (visited_rooms[end][exit_direction] == '?'): 
                    return path
                #when it hasnt been visited run this
                elif (visited_rooms[end][exit_direction] not in visited): 
                    #create a new path
                    new_path = path + [visited_rooms[end][exit_direction]]
                    #add the new path
                    q.enqueue(new_path)
    return path 



# Load world
world = World()



# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)


# Print an ASCII map


world.print_rooms()
player = Player(world.starting_room)


traversal_path = ['n', 's', 'e', 'w']
visited_rooms = {}


#main while loop
while(len(visited_rooms) < len(room_graph)):
    #moving theoretical player through the rooms
    if player.current_room.id not in visited_rooms: 
        enter_room(player.current_room, visited_rooms)

    #creating a list of exits
    exits = []
    #best way to get rid of the '?'
    for new_direction in visited_rooms[player.current_room.id]:
        if (visited_rooms[player.current_room.id][new_direction] == '?'): 
            exits.append(new_direction)
    
    #for the case that the length of exits is 0 
    if (len(exits) == 0): 
        path = bfs(visited_rooms)

        for id in path: 
            for exit_direction in visited_rooms[player.current_room.id]: 
                if (exit_direction in visited_rooms[player.current_room.id]): 
                    #comparing the rooms id's
                    if (visited_rooms[player.current_room.id][exit_direction] == id and player.current_room.id != id):
                        #appending the exit direction to traversal path
                        traversal_path.append(exit_direction)
                        new_room = player.current_room.get_room_in_direction(exit_direction)
                        #setting new room id
                        visited_rooms[player.current_room.id][exit_direction] = new_room.id
                        #checking if new room id isn't in visited...
                        if (new_room.id not in visited_rooms):
                            #enter this room using enter_room
                            enter_room(new_room, visited_rooms)
                        #using the reverse method to get back to original point and find new exits
                        visited_rooms[new_room.id][reverse(exit_direction)] = player.current_room.id
                        #instruct player to move to the exit
                        player.travel(exit_direction)

    else: 
        #search for new exits using random
        new_exit = random.choice(exits)
        #add the exit to traversal
        traversal_path.append(new_exit)
        #find exit in new room
        new_room = player.current_room.get_room_in_direction(new_exit)
        #setting our new room id to that room
        visited_rooms[player.current_room.id][new_exit] = new_room.id 
        # check if the new rooms id is not in the visited rooms
        if (new_room.id not in visited_rooms): 
            #make the player move into that room
            enter_room(new_room, visited_rooms)
        # now utilize the reverse method once again
        visited_rooms[new_room.id][reverse(new_exit)] = player.current_room.id 
        #move player to newly found exit
        player.travel(new_exit)              




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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

print("should be seeing something here")

