import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph():
    def __init__(self, player):
        self.rooms = {}
        self.player = player
        self.traversal_path = []

    def add_room(self, room_id, exits):
        if room_id not in self.rooms:
            self.rooms[room_id] = [{}, ()]
            for exit in exits:
                self.rooms[room_id][0][exit] = '?'
        if room_id == 0:
            self.rooms[room_id][1] = (0, 0)

    def add_connection(self, room1_id, room2_id, direction):
        opposite_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        if room1_id in self.rooms and room2_id in self.rooms:
            self.rooms[room1_id][0][direction] = room2_id
            self.rooms[room2_id][0][opposite_direction[direction]] = room1_id
        else:
            raise IndexError('Room does not exist,')

    def get_exits(self, room_id):
        return self.rooms[room_id][0]

    def get_coordinates(self, room_id):
        return self.rooms[room_id][1]

    def use_exit(self, direction):
        previous_room = self.player.current_room
        self.player.travel(direction)
        self.traversal_path.append(direction)

        new_room = self.player.current_room
        self.add_room(new_room.id, new_room.get_exits())
        self.add_connection(previous_room.id, new_room.id, direction)

        old_coordinates = self.get_coordinates(previous_room.id)

        if direction == 'n':
            new_coordinates = (old_coordinates[0], old_coordinates[1] + 1)
        if direction == 's':
            new_coordinates = (old_coordinates[0], old_coordinates[1] - 1)
        if direction == 'w':
            new_coordinates = (old_coordinates[0] - 1, old_coordinates[1])
        if direction == 'e':
            new_coordinates = (old_coordinates[0] + 1, old_coordinates[1])

        self.rooms[new_room.id][1] = new_coordinates
        self.check_coordinates()

        return new_room

    def dft_recursive(self, starting_room=None, completed=None):
        starting_room = starting_room or self.player.current_room
        completed = completed or set()

        if starting_room not in completed:
            self.add_room(starting_room.id, starting_room.get_exits())

            current_room_id = starting_room.id
            current_exits = self.get_exits(current_room_id)

            directions = ['s', 'w', 'n', 'e']

            random.shuffle(directions)

            if directions[0] in current_exits and current_exits[directions[0]] == '?':
                new_room = self.use_exit(directions[0])
                self.dft_recursive(new_room, completed)
            elif directions[1] in current_exits and current_exits[directions[1]] == '?':
                new_room = self.use_exit(directions[1])
                self.dft_recursive(new_room, completed)
            elif directions[2] in current_exits and current_exits[directions[2]] == '?':
                new_room = self.use_exit(directions[2])
                self.dft_recursive(new_room, completed)
            elif directions[3] in current_exits and current_exits[directions[3]] == '?':
                new_room = self.use_exit(directions[3])
                self.dft_recursive(new_room, completed)
            else:
                completed.add(starting_room)

    def bfs(self, starting_room=None):
        starting_room = starting_room or self.player.current_room
        queue = Queue()
        queue.enqueue([starting_room.id])
        visited = set()

        while queue.size() > 0:
            self.add_room(starting_room.id, starting_room.get_exits())

            current_path = queue.dequeue()
            current_room_id = current_path[-1]
            current_exits = self.get_exits(current_room_id)

            if '?' in current_exits.values():
                self.convert_path_to_directions(current_path)
                return

            if current_room_id not in visited:
                visited.add(current_room_id)
                for exit in current_exits:
                    path_to_next_room = [*current_path, current_exits[exit]]
                    queue.enqueue(path_to_next_room)

    def convert_path_to_directions(self, list_rooms):
        steps_in_path = len(list_rooms) - 1
        for index in range(steps_in_path):
            current_exits = self.get_exits(list_rooms[index]).items()
            next_room = list_rooms[index + 1]
            direction = next(
                (direction for direction, room in current_exits if room == next_room), None)
            self.player.travel(direction)
            self.traversal_path.append(direction)
            self.check_coordinates()

    def check_coordinates(self, starting_room=None):
        starting_room = starting_room or self.player.current_room

        current_coordinates = self.get_coordinates(starting_room.id)
        current_exits = self.get_exits(starting_room.id)
        current_room_id = starting_room.id

        directions = ['n', 's', 'e', 'w']

        if directions[0] in current_exits and current_exits[directions[0]] == '?':
            coordinates_to_check = (
                current_coordinates[0], current_coordinates[1] + 1)
            self.check_for_adjacent_room(
                current_room_id, coordinates_to_check, directions[0])

        if directions[1] in current_exits and current_exits[directions[1]] == '?':
            coordinates_to_check = (
                current_coordinates[0], current_coordinates[1] - 1)
            self.check_for_adjacent_room(
                current_room_id, coordinates_to_check, directions[1])

        if directions[2] in current_exits and current_exits[directions[2]] == '?':
            coordinates_to_check = (
                current_coordinates[0] + 1, current_coordinates[1])
            self.check_for_adjacent_room(
                current_room_id, coordinates_to_check, directions[2])

        if directions[3] in current_exits and current_exits[directions[3]] == '?':
            coordinates_to_check = (
                current_coordinates[0] - 1, current_coordinates[1])
            self.check_for_adjacent_room(
                current_room_id, coordinates_to_check, directions[3])

    def check_for_adjacent_room(self, current_room_id, adjacent_coordinates, direction):
        room_id = next(
            (id for id, value in self.rooms.items() if value[1] == adjacent_coordinates), None)

        if room_id:
            self.add_connection(current_room_id, room_id, direction)