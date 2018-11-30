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
		ranges = len(names)-1
		copy = numUsers
		while copy > 0:
			self.addUser(names[random.randint(0,ranges)])
			copy = copy - 1
        # Create friendships
		copy = numUsers
		friendNums = list()
		high,low = avgFriendships,avgFriendships
		if avgFriendships%2 == 1:
			friendNums.append(avgFriendships)
			copy = copy - 1
		while low > 1:
			low = low -1
			high = high +1
		i = 0
		while copy/2 > i:
			num = random.randint(low,high)
			if num > avgFriendships:
				friendNums.append(num)
				friendNums.append(num-avgFriendships)
			elif num == avgFriendships:
				friendNums.append(num)
				friendNums.append(num)
			else:
				friendNums.append(num)
				friendNums.append(num+avgFriendships)
			i = i + 1
		length = len(self.users)
		print(friendNums)
		for j in range(1,length):
			already_added = set()
			for k in range(0,friendNums.pop(0)):
				f = random.randint(1,length)
				while f == j or f in already_added:
						f = random.randint(1,length)
				print("{}, {}".format(j,f))
				self.addFriendship(j,f)
				already_added.add(f)
			
			
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
