from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

import sys
import argparse
from collections import deque


def get_direction(room):
    """Return a room's first unvisited direction"""
    for direction in ['w', 'n', 'e', 's']:
        visited = room.get(direction)
        if visited == '?':
            return direction
    return None


def bfs(room_id, graph):
    # initialize queue
    qq = deque()
    qq.append([room_id])
    explored = set()
    # print('queue', qq)

    while qq:
        # FIFO queue
        path = qq.popleft()
        room_id = path[-1]

        # print('path:', path)
        # print('room id:', room_id)

        # Exit condition: if found an unvisited room, return the path
        if get_direction(graph[room_id]):
            go_back = []
            for i in range(1, len(path)):
                for room_direction, room_id in graph[path[i-1]].items():
                    if room_id == path[i]:
                        go_back.append(room_direction)
                        break
            # print('go back:', go_back)
            return go_back
            

        if room_id not in explored:
            explored.add(room_id)
            # Then add a path to all unvisited rooms to the back of the queue
            for next_room_id in graph[room_id].values():
                if next_room_id not in explored:
                    qq.append(path + [next_room_id])
    return None


def traverse(player, traversal_path, search_func):
    # dict to reverse directions
    reverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

    # add first room to graph
    graph = {player.current_room.id: {}}

    # initialize exits
    for exits in player.current_room.get_exits():
        graph[player.current_room.id][exits] = '?'
    
    # enter a room in an unvisited direction
    direction = get_direction(graph[player.current_room.id])

    # print(direction)

    # save previous room
    prev_room = player.current_room

    # travel one step and append to traversal path
    player.travel(direction)
    traversal_path.append(direction)

    while True:
        # add room to graph and initialize exits to ?
        if player.current_room.id not in graph:
            graph[player.current_room.id] = {}
            for exits in player.current_room.get_exits():
                graph[player.current_room.id][exits] = '?'
        
        # connect the the current room to previous room
        if graph[player.current_room.id][reverse[direction]] == '?':
            graph[player.current_room.id][reverse[direction]] = prev_room.id
            graph[prev_room.id][direction] = player.current_room.id

        # get available directions
        direction = get_direction(graph[player.current_room.id])
        if direction:
            # if there's an unvisited exit, move to the new room
            prev_room = player.current_room
            player.travel(direction)
            traversal_path.append(direction)
        else:
            # find unvisited room
            # print('graph:', graph)
            return_path = search_func(player.current_room.id, graph)
            # exit case: no unvisited rooms
            if return_path is None:
                break
            # go to unvisited room
            while return_path:
                direction = return_path.pop(0)
                player.travel(direction)
                traversal_path.append(direction)

    return graph


# TRAVERSAL TEST
def traversal_test(player, world, traversal_path):
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



if __name__ == "__main__":

    search_func = bfs

    # map_file = "maps/test_line.txt"
    # map_file = "maps/test_cross.txt"
    # map_file = "maps/test_loop.txt"
    # map_file = "maps/test_loop_fork.txt"
    map_file = "maps/main_maze.txt"

    # initialize world
    world = World()
    room_graph=literal_eval(open(map_file, "r").read())
    world.load_graph(room_graph)

    # Print an ASCII map
    # world.print_rooms()

    # initialize player
    player = Player(world.starting_room)

    # initialize traversal path    
    traversal_path = []

    # traverse graph
    graph = traverse(player, traversal_path, search_func)

    # test traversal
    traversal_test(player, world, traversal_path)
