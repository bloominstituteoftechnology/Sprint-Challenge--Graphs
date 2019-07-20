from collections import deque
import random

class MapGraph:
    def __init__(self):
        self.rooms = {}

    def addRoom(self, roomID):
        if roomID not in self.rooms:
            self.rooms[roomID] = {}
    
    def addExits(self, roomID, exits):
        if roomID not in self.rooms:
            self.addRoom(roomID)
        
        self.rooms[roomID].update(exits)
    
    def exploreMap(self):
        pass

    def findUnexploredRoom(self):
        pass
