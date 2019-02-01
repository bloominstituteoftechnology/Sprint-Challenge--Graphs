class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
    def travel(self, direction, showRooms = False):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            return True
            if (showRooms):
                nextRoom.printRoomDescription(self)
        else:
            print("You cannot move in that direction.")
            return False
