import random
import math

## my helper class queue
class Queue:
    def __init__(self):
        self.storage = []
    
    # enqueue method
    def enqueue(self, value):
        self.storage.append(value)

    # dequeue method
    def dequeue(self):
        return self.storage.pop(0) if self.size() > 0 else None


    # size method
    def size(self):
        return len(self.storage)

    # for indexing
    def __getitem__(self, index):
        return self.storage[index]

    def __setitem__(self, index):
        return self.storage[index]


class User:
    def __init__(self, name, interests):
        self.name = name
        self.interests = []

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
        # range based for loop from zero to numUsers
        for index in range(0, numUsers):
            #call self.add user and do a format string to create the username
            self.addUser("User %i".format(index))

        # Create friendships
        # creat a list of friendships
        friendships_list = []

        # make a for in loop extracting userID from the objects users
        for userID in self.users:
        # make a nested range based loop using the userid and the last id of the current object
        # add the user id and the friend id to the friendship list
        # and shuffle them to randomize
            for friendID in range(userID + 1, self.lastID +1):
                friendships_list.append((userID, friendID))
        random.shuffle(friendships_list)

        # create a second range based loop using the algorithim i said in the answer to the first question in the readme
        # and set the friendship to the current index , invoke the addfriendship method on the current object
        # linking friendship at index of 0 to friendship at index of 1
        for index in range(0, math.floor(numUsers * avgFriendships / 2)):
            friendship = friendships_list[index]
            self.addFriendship(friendship[0], friendship[1])


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
       
       # create a new Queue using my queue class from the routing.py
        queue = Queue()

        # add the userid in to a list and queue it up
        queue.enqueue([userID])

        ## while the queue size is larger than 0 (is not empty)
        ## create a base path
        # set a new user id using the end of the path
        while queue.size() > 0:
            path = queue.dequeue()
            newUserID = path[-1]

            # if visited does not conmtain the new user id then add the path at the index of the new user id
            if newUserID not in visited:
                visited[newUserID] = path
                # do a for in loop over the friendships at the index of the new user id
                for friendID in self.friendships[newUserID]:
                    # if visited does not contain the friend id then create a new list from the path
                    # and append the friend id to it and add the new path to the queue 
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        queue.enqueue(new_path)
        # finally return the visited dictionary     
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
#####################################
## reference for weighted graphing stretch
class UserGraph:
    def __init__(self, width, height, hasCommonInterests):
        self.width = width
        self.height = height
        self.users = {}
        self.common_interests = hasCommonInterests
    
    def common(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()
        results = filter(self.common_interests, results)
        return results


### the startings of a weighted user graph
class WeightedUserGraph(UserGraph):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}
    ## added a costings
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)
#######################################################