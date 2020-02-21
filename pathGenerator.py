#!/usr/bin/env python3

from room import Room
from world import World

import sys
sys.path.append('structs/')
from Queue import Queue


class PathGenerator():
    def __init__(self, worldmap):
        self.worldmap = worldmap

    def generatePath(self):
        superPath = [0]
        paths = self.deadEndPathsFromRoom(0)
        for path in paths:
            superPath += self.shortestAbsolutePath(superPath[-1], path[-1])[1:]
            location = path[-1]
        print(superPath)

        return self.absolutePathToRelative(superPath)

    def unvisitedRooms(self, visited):
        rooms = self.worldmap.rooms.copy()
        for room in visited:
            del rooms[room]
        return rooms.keys

    def shortestRelativePath(self, fromRoom, toRoom):
        path = self.shortestAbsolutePath(fromRoom, toRoom)
        return self.absolutePathToRelative(path)

    def shortestAbsolutePath(self, fromRoom, toRoom):
        # bfs
        q = Queue()
        q.enqueue([fromRoom])

        visited = set()

        while q.size() > 0:
            # print(visited)
            path = q.dequeue()
            roomID = path[-1]

            if roomID == toRoom:
                return path
            if roomID not in visited:
                visited.add(roomID)
                room = self.worldmap.getRoom(roomID)
                # print(roomID, room)
                adjacentRooms = [x for x in [room.n_to, room.e_to, room.s_to, room.w_to] if x is not None]
                if len(path) > 1:
                    prevID = path[-2]
                    adjacentRooms = [x for x in adjacentRooms if x.id != prevID]
                    # print("not including previd:", prevID)
                # print(f"adjacent to {roomID}: {adjacentRooms}")
                for adjacent in adjacentRooms:
                    newPath = path.copy()
                    newPath.append(adjacent.id)
                    q.enqueue(newPath)
        return None

    def absolutePathToRelative(self, path):
        relPath = []

        if path is not None:
            for index in range(len(path) - 1):
                roomID = path[index]
                destRoomID = roomID
                offset = 1
                while destRoomID == roomID:
                    destRoomID = path[index + offset]
                    offset += 1
                originRoom = self.worldmap.getRoom(roomID)
                destRoom = self.worldmap.getRoom(destRoomID)
                direction = originRoom.directionOfRoom(destRoom)
                if direction is None:
                    raise IndexError(f"Room {originRoom.id} not connected to Room {destRoom.id}")
                relPath.append(direction)
        return relPath

    def shortestDirectionRouteFromRoom(self, roomID):
        pass

    def deadEndPathsFromRoom(self, roomID=0, visited=None):
        q = Queue()
        q.enqueue([roomID])
        if visited is None:
            visited = set()

        paths = set()
        while q.size() > 0:
            path = q.dequeue()
            roomID = path[-1]
            if roomID not in visited:
                paths.add(tuple(path))
                visited.add(roomID)
                room = self.worldmap.getRoom(roomID)
                adjacentRooms = [x for x in [room.n_to, room.e_to, room.s_to, room.w_to] if x is not None]
                for adjacent in adjacentRooms:
                    newPath = path.copy()
                    newPath.append(adjacent.id)
                    q.enqueue(newPath)

        pathsList = list(paths)
        pathsList.sort(key=len, reverse=True)

        for pathTup in pathsList:
            path = list(pathTup)
            while len(path) > 0:
                path.pop()
                tTuple = tuple(path)
                if tTuple in paths:
                    paths.remove(tuple(path))

        def mySort(elem):
            value = 0
            for i in range(len(elem)):
                div = 0.1 / ((10 * i) + 1)
                value += div
            total = elem[1] + value
            # print(elem[1], "value: ", value, total)
            return total
        pathsList = list(paths)
        pathsList.sort(key=mySort)
        
        return pathsList

    def complexityFromRoomGoingToward(self, roomID, towardRoomID, visited=None):
        towardRoom = self.worldmap.getRoom(towardRoomID)
        room = self.worldmap.getRoom(roomID)
        connections = towardRoom.connections()
        for direction, room in connections.items():
            if room.id == roomID:
                del connections[direction]

        if len(connections) == 0:
            return 1
        if len(connections) == 1:
            nextRoomID = connections.keys[0].id
            return self.complexityFromRoomGoingToward(towardRoomID, nextRoomID, visited)
        



# note direction came from
# if at an intersection
#   calculate shortest route (in directions not explored)
#       check to see if contains intersections, loop with intersections, or simple dead end
#       if has intersections, sum all child costs
#       if a single dead end, cost is 2x
#       if a simple loop, cost is 1x
#   follow shortest route
#   if there are still unvisited rooms
#       if route was simple dead end
#           retrace steps back to previous intersection first
#       find closest unvisited room (bfs)


# recursive alt
