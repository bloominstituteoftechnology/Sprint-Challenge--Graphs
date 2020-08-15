from room import Room
from player import Player
from world import World

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

opposite_path = {
    'n': 's',
    'e': 'w',
    's': 'n',
    'w': 'e',
}

# init graph
graph = {}

# Init Stack
class Stack():
    def __init__(self):
        self.stack = []

    # Add to Stack
    def push(self, value):
        self.stack.append(value)

    # Remove from stack
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

    # Return Stack size
    def size(self):
        return len(self.stack)

# Int Queue 
class Queue():
    def __init__(self):
        self.queue = []

    # Remove from queue
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)

    # Add to queue
    def enqueue(self, value):
        self.queue.append(value)
       
    # Length of queue
    def size(self):
        return len(self.queue)

def bfs(graph, starting_room):
    # Init queue
    q = Queue()
    # Store visited rooms
    visited = set()
    # Start path adding first vert to queue
    q.enqueue([starting_room])
    # If vert(s) in queue
    while q.size():
        # Remove first vert
        route = q.dequeue()
        # Get last vert added to path
        vertex = route[-1]
        # If vert unvisited, not in  set()
        if vertex not in visited:
            # Mark vert visited, add to set()
            visited.add(vertex)
            # Look for unvisited adjacent verts
            for vert in graph[vertex]:
                # print(vert)
                # If unvisited verts found
                if graph[vertex][vert] == '?':
                    # print(graph[vertex])
                    # Return route
                    return route

            for adjacent_verts in graph[vertex]:
                # Store adjacent verts
                surrounding_verts = graph[vertex][adjacent_verts]
                # !! New route 
                new_route = list(route)
                # Add adjacent vert to new route
                new_route.append(surrounding_verts)
                # Enqueue route
                q.enqueue(new_route)

# While no. of vertices are less than 500
while len(graph) < len(room_graph):
    # Save vert id
    cur_vert_id = player.current_room.id
    # If vert id not in graph
    if cur_vert_id not in graph:
        # Put vert in graph
        graph[cur_vert_id] = {}
        # For all adjacent vertices
        for vert_exits in player.current_room.get_exits():
            # Set to ? while unvisited
            graph[cur_vert_id][vert_exits] = "?"
    
    for direction in graph[cur_vert_id]:
        # Break route if direction cannot be traversed
        if direction not in graph[cur_vert_id]:
            break
        # If direction can be traveled 
        if graph[cur_vert_id][direction] == '?':
            # Set available vert as next direction
            available_vert = direction
            
            if available_vert is not None:
                # Add direction traveled to traversal_path
                traversal_path.append(available_vert)
                # Move to vertex
                player.travel(available_vert)
                # Set vertex id to the cur vertex
                new_vert_id = player.current_room.id
                # If new_vert_id not yet in graph 
                if new_vert_id not in graph:
                    # Add to graph 
                    graph[new_vert_id] = {}
                    # For all unvisited adjacent verts
                    for vert_exits in player.current_room.get_exits():
                        # Set to ?
                        graph[new_vert_id][vert_exits] = '?'
            # Set prev vert direction
            graph[cur_vert_id][available_vert] = new_vert_id
            # Set cur verts opposite direction
            graph[new_vert_id][opposite_path[available_vert]] = cur_vert_id
            # Set cur vert id to the new vert id
            cur_vert_id = new_vert_id

    vert_traversal = bfs(graph, player.current_room.id)
    # Store path of verts traversed
    if vert_traversal is not None:
        # For verts in vert_traversal
        for v in vert_traversal:
            # For all directions available for each vertex
            for vert_exits in graph[cur_vert_id]:
                # If vert_exit is vertex in vert_traversal
                if graph[cur_vert_id][vert_exits] == v:
                    # Add vert_exits to traversal list
                    traversal_path.append(vert_exits)
                    # Move in that direction
                    player.travel(vert_exits)
    # Update the current vert id to vertex just traversed
    cur_vert_id = player.current_room.id


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
