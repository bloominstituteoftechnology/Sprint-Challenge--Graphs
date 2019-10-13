#!/usr/bin/env python

from room import Room
from player import Player
from world import World
from dungeon_lib import roomGraph5 as roomGraph
from datastructures import Stack, Queue

from random import choice
from collections import defaultdict, OrderedDict
from typing import Dict, List, Set, Tuple
# Load world
world = World()


world.loadGraph(roomGraph)
world.printRooms()
player = Player("Name", world.startingRoom)


room_graph = {key: value[1] for key, value in roomGraph.items()}
DIRECTIONS = ('n', 's', 'e', 'w')
build_graph = defaultdict(lambda: {direction: '?' for direction in DIRECTIONS})
build_graph[0]

# FILL THIS IN
traversalPath = ['n', 's']

step_back = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

#print(room_graph)
print()
# print(build_graph)

def bf_paths(graph: Dict[int, Dict[str, int]], starting_room: int) -> Dict[int, List[str]]:
    qq = Queue()
    visited = set()
    qq.enqueue([starting_room])

    paths = {(starting_room,starting_room): [starting_room]}

    while qq.size > 0:
        path: List[int] = qq.dequeue()
        room = path[-1]

        if room not in visited:

            visited.add(room)
            for move, nextroom in graph[room].items():
                path_copy = path.copy()
                path_copy.append(nextroom)
                qq.enqueue(path_copy)

                paths[(starting_room, nextroom)] = paths[(starting_room, room)] + [move]

    paths = {key: val[1:] for key, val in paths.items()}
    return paths

def df_paths(graph: Dict[int, Dict[str, int]], starting_room: int) -> Dict[int, List[str]]:
    ss = Stack()
    visited = set()
    ss.push([starting_room])

    paths = {(starting_room,starting_room): [starting_room]}

    while ss.size > 0:
        path: List[int] = ss.pop()
        room = path[-1]
        if room not in visited:
            visited.add(room)
            for move, nextroom in graph[room].items():
                path_copy = path.copy()
                path_copy.append(nextroom)
                ss.push(path_copy)

                paths[(starting_room, nextroom)] = paths[(starting_room, room)] + [move]

    paths = {key: val[1:] for key, val in paths.items()}
    return paths

def get_ord_list_items_from_dict_paths(paths: Dict[int, List[str]]) -> List[Tuple[int, List[str]]]:

    max_path = max(len(path) for key, path in paths.items())
    paths_sorted = sorted(paths.items(), key=lambda kv: max_path - len(kv[1]))


    paths_ = OrderedDict(paths_sorted)
    return list(paths.items())

PATHS_UNORDERED = bf_paths(room_graph, 0)
PATHS_ITEMS = get_ord_list_items_from_dict_paths(PATHS_UNORDERED)

visited = set()
traversal = list()
curr_room = 0
visited.add(curr_room)
def unvisited() -> Set[int]:
    global visited
    global roomGraph
    return list(set(roomGraph.keys()) - visited)
# while len(visited) != len(roomGraph):
while len(unvisited()) > 0:

    paths__ = bf_paths(room_graph, curr_room)
    paths_ = get_ord_list_items_from_dict_paths(paths__)
    paths = [(key, value) for key, value in paths_ if key[1] in unvisited()]

    start_end, path = paths.pop(0)

    start, end = start_end
    if end not in visited: #and len(room_graph[end]) == 1:

        midpoint = sorted(unvisited()).pop() # choice(unvisited()

        backtracking = bf_paths(room_graph, end)[(end, midpoint)]

        for move in path + backtracking: # REV_PATHS[(end, start)]:
            nextroom = room_graph[curr_room][move]
            visited.add(nextroom)
            traversal.append(move)

            curr_room = nextroom
            if len(visited)==len(roomGraph):
                break
    #break

#hile len(visited) != len(roomGraph):
#
#   Paths = df_paths(room_graph, curr_room)
#
#   random = choice(unvisited())
#   path = Paths[(curr_room, random)]
#
#   for move in path + bf_paths(room_graph, random)[(random, curr_room)]:
#       nextroom = room_graph[curr_room][move]
#       visited.add(nextroom)
#       traversal.append(move)
#       curr_room = nextroom
#
#       if len(visited) == len(roomGraph):
#           break
#   # break

traversalPath = traversal
# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom.id)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom.id)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms. For reference, you made {len(traversalPath)} moves. ")
