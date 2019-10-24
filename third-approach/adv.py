from room import Room
from player import Player
from world import World
from dungeon_lib import roomGraph5 as roomGraph # examination will be on number 5
# from datastructures import Walker, load_graph
from logic import load_graph, walk
import random
from typing import List, Dict, Any
from datastructures import Queue, Stack
# Load world
world = World()

world.loadGraph(roomGraph)
world.printRooms()
player = Player("Quinn", world.startingRoom)

# FILL THIS IN
traversalPath = ['n', 's']

build_up = {k: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
            for k
            in range(len(roomGraph.keys()))
}

room_graph = {key: value[1] for key, value in roomGraph.items()}
reverse = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

#print(room_graph)

#traversal = list()
#
#ooms_neighbs = list(room_graph.items())
#oom, neighbs = rooms_neighbs.pop(0)
#hile rooms_neighbs:
#
#   nsew = list(neighbs.keys())
#   random_dir = random.choice(nsew)
#   random_neighb = neighbs[random_dir]
#   #print(random_dir, random_neighb)
#   if random_neighb != '?':
#       build_up[room][random_dir] = random_neighb
#       traversal.append(random_dir)
#       room, neighbs = rooms_neighbs.pop(0)
   
#print(build_up)
#print(traversal)
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
traversalPath = list()
ss = Stack()
qq = Queue()

while len(visited_rooms) != len(roomGraph.keys()):
    move = random.choice(player.currentRoom.getExits())

    if room_graph[player.currentRoom.id][move] not in visited_rooms:
        ss.push(move)
        while ss.size > 0:
            dir_move: str = ss.pop()

            if dir_move in room_graph[player.currentRoom.id].keys():

                if room_graph[player.currentRoom.id][dir_move] not in visited_rooms:
                    print(dir_move)
                    player.travel(dir_move)
                    traversalPath.append(dir_move)
                    visited_rooms.add(player.currentRoom.id)
                    for mv in player.currentRoom.getExits():

                        if mv in room_graph[player.currentRoom.id].keys():
                            print("     ", mv)
                            if room_graph[player.currentRoom.id][mv] not in visited_rooms:
                                ss.push(mv)
                                continue
                            else:
                                ss.push(reverse[mv])
                                continue
                        else:
                            continue
                else:
                    continue


            else:
                continue
    else:
        ss.push(reverse[move])



# traversalPath = traversal.copy()
# # TRAVERSAL TEST
# visited_rooms = set()
# player.currentRoom = world.startingRoom
# visited_rooms.add(player.currentRoom)
# for move in traversalPath:
#     player.travel(move)
#     visited_rooms.add(player.currentRoom)

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
