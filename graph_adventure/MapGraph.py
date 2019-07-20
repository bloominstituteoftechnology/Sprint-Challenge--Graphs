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
        
        for exit in exits:
            self.rooms[roomID].update({exit:'?'})
    
    def updateExits(self, roomID, exits):
        self.rooms[roomID].update(exits)

    def exploreMap(self, player):
        roomStack = []
        roomStack.append(player.currentRoom.id)
        # Make sure this room is added to our graph as well as all the exits
        self.addExits(player.currentRoom.id, player.currentRoom.getExits())

        while len(roomStack) > 0:
            # Let's get the current room off the stack.
            curRoomID = roomStack.pop()
            exits = self.rooms[curRoomID]
            chosenExit = None

            for exit in exits: # Get each key
                # If an exit is unexplored then we choose the first unexplored exit
                if self.rooms[curRoomID][exit] == '?':
                    chosenExit = exit
                    break

            if chosenExit is not None:
                if chosenExit == 'n':
                    previousExit = 's'
                elif chosenExit == 's':
                    previousExit == 'n'
                elif chosenExit == 'e':
                    previousExit == 'w'
                elif chosenExit == 'w':
                    previousExit == 'e'

                print(roomStack)
                print(self.rooms)
                #print(chosenExit)
                player.travel(chosenExit)
                #print(player.currentRoom.id)
                #roomStack.append(curRoomID)
                roomStack.append(player.currentRoom.id)
                print(roomStack)
                self.addExits(player.currentRoom.id, player.currentRoom.getExits())
                self.updateExits(curRoomID, {chosenExit:player.currentRoom.id})
                self.updateExits(player.currentRoom.id, {previousExit:curRoomID})

    def findUnexploredRoom(self, player):
        pass
