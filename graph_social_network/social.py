import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}
    def __str__(self):
        return str(f"users: {self.users}")

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print(f"WARNING: Friendship already exists at firendId{friendID}, userId {userID}")
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

        possible_friends = []

        #here I looped through and got a random of users from 1 to 10
        for i in range(1, numUsers + 1):
            possible_friends.append(i)

        #here I will make my list of users
        for i in range(1, numUsers + 1):
            self.addUser('test-name')

        #now that my users list is populated and I have random friendships to append
        #I will make a loop and asign my random friendships for each user

        for i in range(1, numUsers + 1):
            random_num = random.randint(0, 2 * avgFriendships)
            random.shuffle(possible_friends)
            for j in range(0, random_num):

                #so I'm not friends with myself or a repeate a friendship
                if i != possible_friends[j] and i < possible_friends[j]:
                
                    self.addFriendship(i, possible_friends[j])



    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        visited = {}

        q = []
        q.append([userID])
        checked = []
        visited.update({userID: [userID]})

        while len(q) > 0:

            if len(q) > 0:
                path = q.pop(0)

            n = path[-1]

            if n not in checked:
                checked.append(n)
                for i in self.friendships[n]:

                    if n > 1:
                        visited.update({n: list(path)})

                    next_path = list(path)
                    next_path.append(i)
                    q.append(next_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(f'\nfriendships: {sg.friendships}')
    print()
    connections = sg.getAllSocialPaths(1)
    print(f'connections {connections}\n')
