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
        if numUsers < avgFriendships:
            print ('The number of users must be greater than the average number of friendships.')
            return 
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f'Friend #{i+1}')

        # Create friendships
        friendships = []
        friends_left = numUsers*avgFriendships
        total_friends = numUsers*avgFriendships

        for i in range(numUsers):
            if friends_left > 0:
                friends = round(random.random()*(avgFriendships*2))
                friends_left -= friends
                friendships.append(friends)
            elif friends_left <= 0:
                friendships.append(0)

        while sum(friendships) < total_friends:
            for i in range(len(friendships)):
                if friends_left:
                    friendships[i] += 1
                    friends_left -= 1

        while sum(friendships) > total_friends:
            for j in range(len(friendships)):
                if friendships[j] and friends_left:
                    friendships[j] -= 1
                    friends_left += 1

        for user in self.users:
            # current_person = friendships.pop(user-1)
            if friendships[user-1]:
                for new_friend_index in range(len(friendships)):
                    if friendships[new_friend_index] == friendships[user-1]:
                        pass
                    elif friendships[new_friend_index] and friendships[user-1]:
                        if new_friend_index+1 not in self.friendships[user]:
                            self.addFriendship(user, new_friend_index+1)
                            friendships[new_friend_index] -= 1
                            friendships[user-1] -= 1
        



    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for user in self.users:
            self.users[user].parent = None
            self.users[user].visited = False

        self.users[userID].visited = True
        queue = [userID]

        while queue:
            u = queue.pop(0)

            for friend in self.friendships[userID]:
                if not self.users[friend].visited:
                    self.users[friend].visited = True
                    self.users[friend].parent = u
                    queue.append(friend)

        for friend in self.friendships[userID]:
            visited[friend] = [friend]
            while self.users[friend].parent:
                visited[friend].append(self.users[friend].parent)
                friend = self.users[friend].parent
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(25, 4)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
