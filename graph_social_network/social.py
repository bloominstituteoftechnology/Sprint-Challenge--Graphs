import random 
import math

# Queue class
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.queue)

# User = Vertex, Node      
class User:
    def __init__(self, name):
        self.name = name

class Friends:
    def __init__(self, name):
        self.name = name
        self.parent_to = None
        self.childern_to = None
        self.items = []
        self.xy = [0,0]

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        # dictionary of users
        self.users = {}
        # dictionary of friendships
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name) # add to the Users dictionary by ID in order
        self.friendships[self.lastID] = set() # then set their list of friendships to an empty set

    def populateGraph(self, numUsers, avgFriendships):
        #(numUsers = room, avgfr = coords)
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # adding users
        for i in range(0, numUsers):
            # naming each user, like index or id
            self.addUser(f"User {i}")

        possibleFriendships = []
        for userID in self.users:
            # This creating a nested loop, going through all the friends.
            # we are only looking at user ids that are less than our current user id
            # adding them to the list possibleFriendships
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        random.shuffle(possibleFriendships)
        # number of friendships we want to create.
        # prevents users from friending themselves or having duplicates
        for i in range(0, math.floor(numUsers * avgFriendships / 2)):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # just like in the homework we are using a queue to track visited nodes
        # and return a dictionary of the paths
        q = Queue()
        q.enqueue([userID])
        while q.size() > 0:
            path = q.dequeue()
            newUserID = path[-1] # up to last item in path
            if newUserID not in visited:
                # using the Id as key, path = value
                visited[newUserID] = path
                for friendID in self.friendships[newUserID]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        q.enqueue(new_path)
        #return visited
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    # print(len(connections))
    # # we can take the list and calc the len then avg it all out
    # total = 0
    # for friendID in connections:
    #     total += len(connections[friendID])
    # print(total / len(connections))
