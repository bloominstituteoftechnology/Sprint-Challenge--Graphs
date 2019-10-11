class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom

    def travel(self, direction, showRooms=False):
        print(f"this is the direction I got: {direction}")
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        print(f"this is the room in that direction: {nextRoom}")
        if nextRoom is not None:
            self.currentRoom = nextRoom
            if (showRooms):
                nextRoom.printRoomDescription(self)
        else:
            print("You cannot move in that direction.")
