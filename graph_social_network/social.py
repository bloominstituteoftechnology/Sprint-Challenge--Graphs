import random

names = ["bob","steve","dave","zorg, destroyer of worlds","fred","greg","mark"]

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
	def __init__(self):
		self.lastID = 0
		self.users = {}
		self.friendships = {}

	def addFriendship(self, userID, friendID):
		if userID == friendID:
			print("WARNING: You cannot be friends with yourself")
		elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
			print("WARNING: Friendship already exists")
		else:
			self.friendships[userID].add(friendID)
			self.friendships[friendID].add(userID)

	def addUser(self, name):
		self.lastID += 1  # automatically increment the ID to assign the new user
		self.users[self.lastID] = User(name)
		self.friendships[self.lastID] = set()

	def populateGraph(self, numUsers, avgFriendships):
		self.lastID = 0
		self.users = {}
		self.friendships = {}
		range = len(names)-1
		while numUsers > 0:
			self.addUser(names[random.randint(0,range)])
			numUsers = numUsers - 1
        # Create friendships
		
	def getAllSocialPaths(self, userID):
		visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
		return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10,2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
