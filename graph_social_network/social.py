import random
import itertools

import sys
sys.path.insert(0, '../graph_shortest_path')
from routing import Queue

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

        # Add users
        for i in range (0, numUsers):
            self.addUser(f'user{i + 1}')

        # Create friendships
        num_of_friendships =  (numUsers * avgFriendships) / 2
        while num_of_friendships > 0:
            for user in self.users:
                if num_of_friendships <= 0:
                    break
                possible_friends = self.users.copy()
                possible_friends.pop(user)
                rand_num_of_friends = random.randint(0, num_of_friendships)
                rand_pos_friends = list(itertools.combinations(possible_friends, rand_num_of_friends))
                random.shuffle(rand_pos_friends)

                if len(rand_pos_friends) > 0:
                    rand_pos_friends = rand_pos_friends[0]

                    for pos_friend in rand_pos_friends:
                        if pos_friend > user:                    
                            if pos_friend not in self.friendships[user]:
                                self.addFriendship(user, pos_friend)
                                num_of_friendships -= 1

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()
        queue.enqueue([userID])
        while queue.len() > 0:
            user_path = queue.dequeue()
            user = user_path[-1]
            if user not in visited:
                visited[user] = user_path
                for child in self.friendships[user]:
                    new_user_path = list(user_path)
                    new_user_path.append(child)
                    queue.enqueue(new_user_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)


# Questions from the README answered in the README file itself.
