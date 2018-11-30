import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
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
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
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
        # !!!! IMPLEMENT ME

        if avgFriendships > numUsers:
            print("Error: must enter a lower number of average friendships than users.")
            return

        # Add users
        for i in range(1, numUsers):
            self.addUser(i)

        # Create friendships
        for i in range(1, len(self.users)):
            possible_friendships = list(self.users.values())
            random.shuffle(possible_friendships)
            # print(possible_friendships)
            for j in range(avgFriendships):
                if i < possible_friendships[j].name:
                    self.addFriendship(i, possible_friendships[j].name)
                # self.friendships[i].add(possible_friendships[j])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        # the userID passed in retrns a search-style traversal output, starting with itself and outputting additional connections until it reaches each UserID

        for i in range(1, len(self.users)):
            # run a bfs and append to dictionary in format: visited[i] = bfs_results

            queue = Queue()
            queue.add([self.users[userID].name])
            # print(self.users[userID].name)
            # print(userID)

            while queue.size() > 0:
                current_node = queue.pop()
                if len(current_node) > len(self.users):
                    queue = Queue()
                    break
                elif current_node[-1] == i:
                    visited[i] = current_node
                    queue = Queue()
                    queue.add([self.users[userID].name])
                    break
                # traversal_path.append(current_node[-1])
                for item in self.friendships[current_node[-1]]:
                    new_path = list(current_node)
                    new_path.append(item)
                    queue.add(new_path)

        return visited

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def __repr__(self):
        pretty_print = "" # actually conventionally a separator character
        return pretty_print.join(str(self.queue))



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
