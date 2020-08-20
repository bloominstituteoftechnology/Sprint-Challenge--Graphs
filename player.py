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
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        #while q is not empty 
        while q.size() > 0:
            # dq the first PATH (list)
            path = q.dequeue()
            # grab the last vertex from the PATH
            v = path[-1]
            # check if the vertex has not been visited
            if v not in visited:
                # is this the destination
                if v == destination_vertex:
                    # return path
                    return path
                # mark as visited
                visited.add(v)
                # then add a path to its neighbors to the back of the queue
                for next_v in self.get_neighbors(v):
                    # make a copy of the path
                    path_copy = list(path)
                    # append neighbor to the back
                    path_copy.append(next_v)
                    # enqueue new path
                    q.enqueue(path_copy)
        return None