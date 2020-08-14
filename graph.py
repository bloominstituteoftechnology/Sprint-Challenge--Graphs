class Graph:
    """docstring for Graph."""

    def __init__(self, player):
        self.rooms = {}
        self.graph = []
        self.player = player

    # Add a room (vertex) to graph
    def add_room(self, room_id, exits):
        if room_id not in self.rooms:
            self.rooms[room_id][exits] = "?"

    # add directed exits (edges) to graph
    def add_exits(self, room1, room2, direction):
        opposite_direction = {'n': 's', 's': 'n', 'e': 'w', 'w':'e'}
        if room1 in self.rooms and room2 in self.rooms:
            self.rooms[room1][direction] = room2
            self.rooms[room2][opposite_direction[direction]] = room1
        else:
            raise IndexError('That room does not exits!')

    # get all exits (edges) of a room (vertex)
    def get_exits(self, room_id):
        return self.rooms[room_id]

    # Navigate to next room given input of direction
    def take_exit(self, direction):
        print(f'{direction} exit unexplored, traveling {direction}')
        print('---')
        room_leaving = self.player.current_room
        self.player.travel(direction)
        self.graph.append(direction)
        new_room = self.player.current_room
        self.add_room(new_room.id, new_room.get_exits())
        self.add_exits(room_leaving.id, new_room.id, direction)
        return new_room

    def dfs(self, starting_room=None, finished=None):
        starting_room = starting_room or self.player.current_room
        finished = finished or set()

        if starting_room not in finished:
            self.add_room(starting_room.id, starting_room.get_exits())

            current_room_id = starting_room.id
            current_exits = self.get_exits(current_room_id)

            print('Current Room:', current_room_id)
            print('Exits:', current_exits)

            if 'n' in current_exits and current_exits['n'] == '?':
                new_room = self.take_exit('n')
                self.dfs(new_room, finished)
            elif 'e' in current_exits and current_exits['e'] == '?':
                new_room = self.take_exit('e')
                self.dfs(new_room, finished)
            elif 's' in current_exits and current_exits['s'] == '?':
                new_room = self.take_exit('s')
                self.dfs(new_room, finished)
            elif 'w' in current_exits and current_exits['w'] == '?':
                new_room = self.take_exit('w')
                self.dfs(new_room, finished)
            else:
                print('All exits explored!')
                finished.add(starting_room)
