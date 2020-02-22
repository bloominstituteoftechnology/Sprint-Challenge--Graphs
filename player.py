class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            
            # TODO: What is show_rooms doing?? 
            if (show_rooms): 
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")
        
    def __str__(self):
        output = f'-*- START PLAYER __str__() -*b-\n'
        output += f'Player is in room {self.current_room}\n'
        output += f'-*- END PLAYER __str__() -*b-'

        return output
        
