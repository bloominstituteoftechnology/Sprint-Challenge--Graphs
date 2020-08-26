from util import Stack, Queue
from room import Room
from player import Player
from world import World
import random
from ast import literal_eval

class Graph:
    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def dft(self,starting_vertex):
        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            current_node = stack.pop()
            room = current_node[-1]
            if room not in visited:
                self.vertices[room.id] ={}
                for possible_direction in room.get_exits():
                    self.vertices[room.id][room.get_room_in_direction(possible_direction).id]= possible_direction
                visited.add(room)
                exits = room.get_exits()
                while len(exits) > 0:
                    direction = exits[0]
                    neighbor_path = list(current_node)
                    neighbor_path.append(room.get_room_in_direction(direction))
                    stack.push(neighbor_path)
                    exits.remove(direction)
        return self.vertices

    def bfs(self, starting_vertex, destination_vertex):
            """
            Return a list containing the shortest path from
            starting_vertex to destination_vertex in
            breath-first order.
            """
            # create an empty queue
            q = Queue()
            # enqueue path to the starting vertex
            q.enqueue([starting_vertex])
            # create a set to track vertices we have visited
            visited = set()
            # while the queue is not empty
            while q.size() > 0:
                # dequeue the first path
                current_path = q.dequeue()
                # get last vertex from the path
                last_vertex = current_path[-1]
                # if vertex has not been visited:
                if last_vertex not in visited:
                    if last_vertex == destination_vertex:
                        return current_path
                    # mark is as visited
                    visited.add(last_vertex)
                    # enqueue its neightbors
                    for room_id in self.vertices[last_vertex].keys():
                        neighbor_path = list(current_path)
                        # add neighbor room id
                        neighbor_path.append(room_id)
                        # enqueue to continue exploring
                        q.enqueue(neighbor_path)

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
print(player.current_room)
graph = Graph()
# use DFT to create graph map of the world
rooms_obj_dft = graph.dft(player.current_room)
# Extract room_id to a list
rooms_list_dft = [room_id for room_id in rooms_obj_dft.keys()]

print("rooms_list_dft\n{}\n".format("-"*100),rooms_list_dft)
print("rooms_obj_dft\n{}\n".format("-"*100),rooms_obj_dft)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

while(len(rooms_list_dft) > 1):
    # set current room position
    current_room = rooms_list_dft[0]
    next_room = rooms_list_dft[1]
    current_room_neighbors = rooms_obj_dft[current_room]
    # if they are neighbor, add to traversal_path
    if next_room in current_room_neighbors.keys():
        traversal_path.append(current_room_neighbors[next_room])
    else:
        # if they are not neighbor, use bfs to find shortest path between them
        short_path = graph.bfs(current_room,next_room)
        while len(short_path) > 1:
            current_room_neighbors = rooms_obj_dft[short_path[0]]
            next_room = short_path[1]
            # if they are neighbor, add to traversal_path
            if next_room in current_room_neighbors.keys():
                traversal_path.append(current_room_neighbors[next_room])
            else:
                traversal_path.append('?')
            short_path.pop(0)
    rooms_list_dft.pop(0)

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