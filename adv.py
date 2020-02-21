#!/usr/bin/env python3

from room import Room
from player import Player
from world import World
from pathGenerator import PathGenerator
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/test_loop_fork2.txt"
# map_file = "maps/test_loop_fork3.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# print(world.rooms)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

pathGen = PathGenerator(world)


# traversal_path = pathGen.shortestRelativePath(0, 4) + pathGen.shortestRelativePath(4, 0) + pathGen.shortestRelativePath(0, 24) + pathGen.shortestRelativePath(24, 18) + pathGen.shortestRelativePath(18, 11) + pathGen.shortestRelativePath(11, 8) + pathGen.shortestRelativePath(8, 0) + pathGen.shortestRelativePath(0, 2) + pathGen.shortestRelativePath(2, 14) + pathGen.shortestRelativePath(14, 17)
traversal_path = pathGen.generatePath()

print(traversal_path)
# def getLength(elem):
#     return len(elem)

# paths = pathGen.deadEndPathsFromRoom()
# print(pathGen.roomCountFrom(1, 5, set([3, 4])))

# paths.sort(key=getLength)

# for path in paths:
#     print(path)

# loop = pathGen.roomLoopDestinationFrom(0, 3)
# print(loop)
# loop = pathGen.roomLoopDestinationFrom(0, 1)
# print(loop)
# loop = pathGen.roomLoopDestinationFrom(0, 5)
# print(loop)
# loop = pathGen.roomLoopDestinationFrom(0, 7)
# print(loop)


# intersects = pathGen.closestIntersections(0)
# print(intersects)
# intersects = pathGen.closestDeadEnds(0)
# print(intersects)

# complexity = pathGen.intersectionComplexity(0)
# print(complexity)
# complexity = pathGen.intersectionComplexity(8, set([0, 3, 4]))
# print(complexity)
# complexity = pathGen.intersectionComplexity(10, set([0, 3, 4, 7, 8, 25]))
# complexity = pathGen.intersectionComplexity(6, set([0, 3, 4, 7, 8, 25, 9, 10]))
# complexity = pathGen.intersectionComplexity(20, set([0, 3, 4, 7, 8, 25, 9, 10, 11, 6]))

# nearestInter = pathGen.findNearestUnfinishedIntersection(4, set([0, 3, 4]))
# print(nearestInter)
# nearestInter = pathGen.findNearestUnfinishedIntersection(25, set([0, 7, 8]))
# print(nearestInter)
# nearestInter = pathGen.findNearestUnfinishedIntersection(24, set([0, 7, 8, 25, 9, 10, 11, 6, 20, 21, 22, 23, 24]))
# print(nearestInter)

# print(pathGen.isRoomIntersection(6))


# exit()

# TRAVERSAL TEST
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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
