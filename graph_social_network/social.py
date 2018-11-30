import random
import math


class User:
    def __init__(self, name):
        self.name = name


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

    def random_friend_id(self, user_id, numUsers):
        friend_id = random.randint(0, numUsers)
        if user_id == friend_id:
            return self.random_friend_id(user_id, numUsers)
        else:
            return friend_id

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

        # Add users
        for i in range(0, numUsers):
            self.addUser(f'User: {i}')
        # Create friendships

        possibleFriendships = []
        # for userID in self.users:
        #     for friendID in range(userID + 1, self.lastID + 1):
        #         possibleFriendships.append(userID, friendID)
        # random.shuffle(possibleFriendships)
        numFriendships = 0
        numCollisions = 0
        while numFriendships < numUsers * avgFriendships:
            user1 = random.randrange(1, self.lastID + 1)
            user2 = random.randrange(1, self.lastID + 1)
            if not (user1 in self.friendships[user2] or user1 == user2):
                self.addFriendship(user1, user2)
                numFriendships += 2
            else:
                numCollisions += 1
        print(f'num collisions: {numCollisions}')
        # for i in range(0, math.floor(numUsers * avgFriendships / 2)):
        #     friendship = possibleFriendships[i]
        #     self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()

        q.enqueue([userID])
        while q.size > 0:
            path = q.dequeue()
            newUserID = path[-1]
            if newUserID not in visited:
                visited[newUserID] = path
                for friendID in self.friendships[newUserID]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    print(len(connections))
    total = 0
    for friendID in connections:
        total += len(connections[friendID] - 1)
    print(total / len(connections))
