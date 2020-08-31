from utils import Queue, Stack

class Player:
    def __init__(self, starting_room, num_rooms):
        self.current_room = starting_room
        self.seen = {starting_room.id}
        self.num_rooms = num_rooms
        self.traversal_path = []
        
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            self.traversal_path.append(direction)
            self.seen.add(self.current_room.id)
            if (show_rooms):
                next_room.print_room_description(self)

    def find_room(self):
        # implement bfs to find path to nearest unseen room
        
        # def bfs(self, starting_vertex, destination_vertex):
        # """
        # Return a list containing the shortest path from
        # starting_vertex to destination_vertex in
        # breath-first order.
        # """

        # initialize queue with starting vertex
        queue = Queue()
        queue.enqueue((self.current_room, []))
        
        # set to keep track of vertexes already seen
        visited = set()

        # while queue is not empty
        while queue.size() > 0:
            # get path and vertex
            room, path = queue.dequeue()
            # if room has not been seen, return path
            if room.id not in self.seen:
                return path
            # else, add vertex to visited
            elif room.id not in visited:
                visited.add(room.id)      
                # and add paths to the queue for each edge
                for exit in room.get_exits():
                    path_copy = path.copy()
                    path_copy.append(exit)
                    queue.enqueue((room.get_room_in_direction(exit), path_copy))
        
        print('Room not found')

    def start_maze(self):
        while len(self.seen)<self.num_rooms:
            path = self.find_room()
            for direction in path:
                self.travel(direction)
                print(direction, self.current_room.id)