#!/usr/bin/env python

from room import Room
from player import Player
from world import World
from dungeon_lib import roomGraph5 as roomGraph
from datastructures import Stack, Queue

from random import choice
from collections import defaultdict, OrderedDict
from typing import Dict, List
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

def bf_path(graph: Dict[int, Dict[str, int]], starting_room: int) -> Dict[int, List[str]]:
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
    

PATHS_UNORDERED = bf_path(room_graph, 0)
MAX_PATH = max(len(val) for key, val in PATHS_UNORDERED.items())
PATHS_SORTED = sorted(PATHS_UNORDERED.items(), key=lambda kv: len(kv[1]))

PATHS = OrderedDict(PATHS_SORTED)



REV_PATHS = {(key[1], 0): [step_back[mv] for mv in path[::-1]] for key, path in PATHS.items()}

visited = set()
traversal = list()
curr_room = 0
visited.add(curr_room)
while len(visited) != len(roomGraph):
    for start_end, path in list(PATHS.items())[::-1]:
        start, end = start_end
        # print(len(path))
        if end not in visited: #and len(room_graph[end]) == 1:

            # print(end, len(path))
            for move in path + bf_path(room_graph, end)[(end, start)]: # REV_PATHS[(end, start)]:
                #print(curr_room, room_graph[curr_room])
                nextroom = room_graph[curr_room][move]
                visited.add(nextroom)
                traversal.append(move)
                curr_room = nextroom
    break


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
