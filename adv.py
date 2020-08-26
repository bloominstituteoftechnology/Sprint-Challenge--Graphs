from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def dfs(self, starting_vertex):
        # stack stepup
        visited_rooms = set()
        stack = Stack()
        stack.push([starting_vertex])
        # not empty...
        while stack.size() > 0:
            # pop the current room onto the stack
            current_room = stack.pop()
            # set the starting room
            room = current_room[-1]
            # have we visited this room?
            if room not in visited_rooms:
                self.vertices[room.id] = {}
                for direction in room.get_exits():
                    self.vertices[room.id][room.get_room_in_direction(direction).id] = direction
                # add the room to visited
                visited_rooms.add(room)
                # add the neighbors
                exits = room.get_exits()
                while len(exits) > 0:
                    direction = exits[0]
                    # make neighbor
                    neighbor_exit = list(current_room)
                    # add the exits
                    neighbor_exit.append(room.get_room_in_direction(direction))
                    stack.push(neighbor_exit)
                    # remove and continue
                    exits.remove(direction)
        return self.vertices

    def bfs(self, starting_vertex, destination_vertex):
            # new queue
            q = Queue()
            # enqueue starting vertex
            q.enqueue([starting_vertex])
            # new set to track visited vertices
            visited_vertex = set()
            # as long as the queue isnt empty
            while q.size() > 0:
                # dequeue first path
                path = q.dequeue()
                # grab last vertex from path
                last_vertex = path[-1]
                # if we have not visited this vertex
                if last_vertex not in visited_vertex:
                    if last_vertex == destination_vertex:
                        return path
                    # put it in visited
                    visited_vertex.add(last_vertex)
                    # enqueue neightbors
                    for room_id in self.vertices[last_vertex].keys():
                        neighbor_exit = list(path)
                        # add neighbor room id
                        neighbor_exit.append(room_id)
                        # enqueue and continue
                        q.enqueue(neighbor_exit)

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
g = Graph()
room_dfs = g.dfs(player.current_room)
room_list = [room_id for room_id in room_dfs.keys()]
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

while(len(room_list) > 1):
    # set room
    current_room = room_list[0]
    # set next room
    next_room = room_list[1]
    # grab the neighbors, store it here
    current_room_neighbors = room_dfs[current_room]
    # if they are neighbor then its the next path, add to traversal_path
    if next_room in current_room_neighbors.keys():
        traversal_path.append(current_room_neighbors[next_room])
    else:
        # not neighbor? bfs will give use the shortest path between them
        short_path = g.bfs(current_room,next_room)
        # as long as it isnt empty
        while len(short_path) > 1:
            # store these neighbors
            current_room_neighbors = room_dfs[short_path[0]]
            # the next room is the next place in the array, store it!
            next_room = short_path[1]
            # neighbor? add to traversal_path
            if next_room in current_room_neighbors.keys():
                traversal_path.append(current_room_neighbors[next_room])
            else:
                # get rid of the path
                traversal_path.append('?')
            short_path.pop(0)
    room_list.pop(0)




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
