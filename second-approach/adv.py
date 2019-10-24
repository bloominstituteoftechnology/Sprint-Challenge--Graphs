from room import Room
from player import Player
from world import World
from dungeon_lib import roomGraph4 as roomGraph # examination will be on number 5
# from datastructures import Walker, load_graph
from logic import load_graph, walk
import random
from typing import List, Dict, Any

# Load world
world = World()

world.loadGraph(roomGraph)
world.printRooms()
player = Player("Quinn", world.startingRoom)

# FILL THIS IN
traversalPath = ['n', 's']

# print(roomGraph)
graph = load_graph(roomGraph)

visitation_order, traversalPath = walk(graph, 0)


# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
