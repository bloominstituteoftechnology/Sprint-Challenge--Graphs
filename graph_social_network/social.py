import random

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) <= 0
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

        # Add users
        for i in range(0, numUsers):
            self.addUser("Brian-"+str(i+1))

        # Create friendships
        for i in range(0, avgFriendships):
            for u in self.users:
                self.friendships[u].add(random.choice([user for user in self.users]))
            

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        pass


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(20, 3)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(3)
    # print(connections)

    # Questions...
    # 1. Using the algorithm that I used I think it would be linear * avgFriends timed, so O(n*e), so I would need my for-loop to iterate 100 times for the users and then 10 times per user to generate them 10 friends.

    # 2. I think it would be 2.5%. If you have 1000 users and 5 friends each and each friend also has 5 friends, you would have 5^2 which is 25 and 25 is 2.5% of 1000. I could be wrong, but that is my best guess. This is based on Faceboo's friends-of-friends model. I'm not sure about the average degree of seperation, but I'm going to blindly guess that it is 40.
