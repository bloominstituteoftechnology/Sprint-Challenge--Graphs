from random import *


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    def first_item(self):
        if len(self.queue) > 0:
            return self.queue[0]

        return None


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


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
        friends = []

        # Add users
        # Create a new user
        for usr in range(1, numUsers + 1):
            self.addUser(usr)

            # Append user to friends list
            friends.append(usr)

        # Create friendships
        for usr in self.users:
            # Randomly re-order the friends list
            shuffle(friends)

            if usr != friends[0]:
                self.addFriendship(usr, friends[0])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Implement parent and visited properties
        for user in self.users:
            self.users[user].parent = None
            self.users[user].visited = False

        # Set the current user to visited
        self.users[userID].visited = True

        # Add user to queue
        queue = [userID]

        while queue:
            # Set user to u
            u = queue.pop(0)

            # And for each friend in the friendships of the current user
            for friend in self.friendships[userID]:
                # If the friend isn't visited, set visited to true
                if not self.users[friend].visited:
                    self.users[friend].visited = True
                    # Set the parent of that friend to the current user
                    self.users[friend].parent = u
                    # Append to queue
                    queue.append(friend)

            # For each friend of the user
            for friend in self.friendships[userID]:
                # Add friend to the visited dict
                visited[friend] = [friend]

                # While the user's friends have a parent
                while self.users[friend].parent:
                    # Add then to the visited dict
                    visited[friend].append(self.users[friend].parent)
                    # Set friend to the parent and loop again
                    friend = self.users[friend].parent

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

