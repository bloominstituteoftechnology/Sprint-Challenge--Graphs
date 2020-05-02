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
        visited_rooms = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            current_room = stack.pop()
            room = current_room[-1]
            if room not in visited_rooms:
                self.vertices[room.id] = {}
            for direction in room.get_exits():
                self.vertices[room.id][room.get_room_in_direction(direction).id] = direction
            visited_rooms.add(room)
            exits = room.get_exits()
            while len(exits) > 0:
                selected = exits[0]
                neighbor_exit = list(current_room)
                stack.push(neighbor_exit)
                exits.remove(selected)
        return self.vertices

    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue, and enqueue a PATH to the starting vertex
        daQueue = Queue()
        daQueue.enqueue([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while the queue is not empty
        while daQueue.size() > 0:
            # dequeue the first PATH
            path = daQueue.dequeue()
            # grab the last vertex in the path

            # of it hasnt been visited
            if path[-1] not in visited_vertices:
                # check if its the target
                if path[-1] == destination_vertex:
                    # return the path if it is
                    return path
                # mark it as visited
                visited_vertices.add(path[-1])
                # make new versions fo the current path, with each neighbor added to them
                for next_vert in self.get_neighbors(path[-1]):
                    # duplicate the path
                    new_path = list(path)
                    # add the neighbor
                    new_path.append(next_vert)
                    # add the new path to the queue
                    daQueue.enqueue(new_path)

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
    # set current room position
    current_room = room_list[0]
    next_room = room_list[1]
    current_room_neighbors = room_dfs[current_room]
    # if they are neighbor, add to traversal_path
    if next_room in current_room_neighbors.keys():
        traversal_path.append(current_room_neighbors[next_room])
    else:
        # if they are not neighbor, use bfs to find shortest path between them
        short_path = g.bfs(current_room,next_room)
        while len(short_path) > 1:
            current_room_neighbors = room_dfs[short_path[0]]
            next_room = short_path[1]
            # if they are neighbor, add to traversal_path
            if next_room in current_room_neighbors.keys():
                traversal_path.append(current_room_neighbors[next_room])
            else:
                traversal_path.append('?')
            short_path.pop(0)
    room_dfs.pop(0)




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
