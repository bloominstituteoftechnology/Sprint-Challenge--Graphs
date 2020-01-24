from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue:
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


# Explore the unknown or rather find it
def explore(player, moves_cue):
    # init queue
    q = Queue()
    # init set for visited rooms
    visited = set()
    # add current room to queue
    q.enqueue([player.current_room.id])
    # if queue is bigger than 0 there are things to explore
    while q.size() > 0:
        # as path is explored removefrom queue
        path = q.dequeue()
        # keep track of last room visited
        last_room = path[-1]
        # if the last room was not in previously visited
        if last_room not in visited:
            # add to list of visited
            visited.add(last_room)
            # Find all the exits for the room
            for exit in graph[last_room]:
                # if we find an exit in the room that is unexplored
                if graph[last_room][exit] == "?":
                    # add path to list to explore
                    return path
                    # otherwise remove path as already explored
                else:
                    lost = list(path)
                    lost.append(graph[last_room][exit])
                    q.enqueue(lost)
    return []


def q_moves(player, moves_q):
    current_exits = graph[player.current_room.id]
    untried_exits = []
    for direction in current_exits:
        if current_exits[direction] == "?":
            untried_exits.append(direction)
    if len(untried_exits) == 0:
        unexplored = explore(player, moves_q)
        room_num = player.current_room.id
        for next in unexplored:
            for direction in graph[room_num]:
                if graph[room_num][direction] == next:
                    moves_q.enqueue(direction)
                    room_num = next
                    break
    else:
        moves_q.enqueue(untried_exits[random.randint(0, len(untried_exits) - 1)])


attempts = 100
optimum_len = 997
optimum_path = []
for x in range(attempts):
    player = Player(world.starting_room)
    graph = {}

    fresh_room = {}
    for direction in player.current_room.get_exits():
        fresh_room[direction] = "?"
    graph[world.starting_room.id] = fresh_room

    moves_q = Queue()
    total_moves = []
    q_moves(player, moves_q)

    reverse_compass = {"n": "s", "s": "n", "e": "w", "w": "e"}

    while moves_q.size() > 0:
        starting = player.current_room.id
        next = moves_q.dequeue()
        player.travel(next)
        total_moves.append(next)
        end = player.current_room.id
        graph[starting][next] = end
        if end not in graph:
            graph[end] = {}
            for exit in player.current_room.get_exits():
                graph[end][exit] = "?"
        graph[end][reverse_compass[next]] = starting
        if moves_q.size() == 0:
            q_moves(player, moves_q)
    if len(total_moves) < optimum_len:
        optimum_path= total_moves
        optimum_len = len(total_moves)


traversal_path = optimum_path

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")