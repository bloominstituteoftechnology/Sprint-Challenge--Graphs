from util import Queue

class Player:
    def __init__(self, starting_room, rooms):
        self.current_room = starting_room
        # player on load enters the starting room
        self.entered = {starting_room}
        # init rooms
        self.rooms = rooms
        # attach path to player
        self.traversal_path = []
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            # append direction moved
            self.traversal_path.append(direction)
            self.entered.add(self.current_room)
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")
## set up BFS 
    def bfs(self):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue PATH to the starting Vertex ID
        #q.enqueue([starting_vertex]) #making into a list
        q = Queue()
        # em q players current room and list out rooms
        q.enqueue((self.current_room, []))
        # create a set to store visited rooms
        visited = set()
        #while q is not empty 
        while q.size() > 0:
            # dq the first PATH (list)
            current, path = q.dequeue()
            # check if current location has been NOT been entered
            if current not in self.entered:
                return path
            # if current has not been visited add to vistied list
            elif current not in visited:
                visited.add(current)
                for exit in current.get_exits():
                    # make a copy of the path
                    path_copy = path.copy()
                    # append exit to the back
                    path_copy.append(exit)
                    # enqueue new path
                    q.enqueue((current.get_room_in_direction(exit),path_copy))
        raise ValueError("No room in that direction")

    def start_loop(self):
        while len(self.entered) < self.rooms:
            path = self.bfs()
            for direction in path:
                self.travel(direction)
                print(self.current_room)