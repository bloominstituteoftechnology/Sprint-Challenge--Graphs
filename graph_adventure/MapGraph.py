from collections import deque
import random

class MapGraph:
    def __init__(self):
        self.rooms = {}
        self.exploredRoomIDS = []
        self.deadendRoomIDs = []

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
            if len(exits) == 1:
                # Only one exit. This is a deadend room
                self.deadendRoomIDs.append(curRoomID)

            for exit in exits: # Get each key
                # If an exit is unexplored then we choose the first unexplored exit
                if self.rooms[curRoomID][exit] == '?':
                    chosenExit = exit
                    break
                if self.rooms[curRoomID][exit] in self.exploredRoomIDS:
                    pass
            if chosenExit is not None:
                if chosenExit == 'n':
                    previousExit = 's'

                elif chosenExit == 's':
                    previousExit = 'n'

                elif chosenExit == 'e':
                    previousExit = 'w'

                elif chosenExit == 'w':
                    previousExit = 'e'

                player.travel(chosenExit)
                #print(player.currentRoom.id)
                #roomStack.append(curRoomID)
                roomStack.append(player.currentRoom.id)
                
                self.addExits(player.currentRoom.id, player.currentRoom.getExits())
                self.updateExits(curRoomID, {chosenExit:player.currentRoom.id})
                self.updateExits(player.currentRoom.id, {previousExit:curRoomID})
                # DFT works for updating the map.
                # Now need to search for a room with an unknown path in it.
            if chosenExit is None:
                #  No room was picked meaning we've found no unexplored exits. So this room is fully explored
                self.exploredRoomIDS.append(curRoomID)

            if len(roomStack) <= 0:
                # We've run out of rooms to explore. Let's check the current known rooms
                #print(roomStack)
                path = self.findUnexploredRoom(player)
                for direction in path:
                    player.travel(direction)
                    #print(f'currentRoom.id: {player.currentRoom.id}')
                    print(roomStack)
                    roomStack.append(player.currentRoom.id)
                    print(self.rooms)

    def findUnexploredRoom(self, player):
        # We'll search for an unexplored room
        roomQueue = deque()
        roomQueue.append(player.currentRoom.id)
        path = []
        # We're going to queue every known room and look until we find a room with an unknown exit
        while len(roomQueue) > 0:
            curRoomID = roomQueue.popleft()
            lastExit = None
            #print(self.rooms[curRoom])
            # Actually traverse the rooms with the player!
            # Have a check to see if a room is a deadend (only one exit!)
            for exit in self.rooms[curRoomID]:
                if self.rooms[curRoomID][exit] == '?':
                    # We found an unknown room lets return the path to walk to it.
                    return path[:-1]                  
                # We've found a room that's not a deadend. It is fully explored
                else:
                    # This needs to be optimized because it travels down and back before getting to the right path.. but it works ?
                    if exit == 'n':
                        lastExit = 's'
                    elif exit == 's':
                        lastExit = 'n'
                    elif exit == 'e':
                        lastExit = 'w'
                    elif exit == 'w':
                        lastExit = 'e'
                    if exit != lastExit:
                        path.append(exit)
                        roomQueue.append(self.rooms[curRoomID][exit])
                    