#Power Grid Node
#dyshi
class Node:
	#Dict<String ,int>  reachableNodes maps city names to cost
	#Array occupiedPlayers
	#int currentCost the cost to occupy a part of this city
	#int name Unique name identifier
	def __init__(self, name):
		self.name = name
		self.occupiedPlayers = []
		self.reachableNodes = {}
		self.currentCost = 10
	
	#return String the name of this city
	def name(self):
		return self.name

	#return void This method will make a connection given a city and its cost
	#Node city is the unique name of the city
	#int cost is the amount needed to make a connection
	def makeConnection(self, city, cost):
		if (self.reachableNodes.get(city.name) != None):
			raise Exception("Connection already made for " + city.name)
		self.reachableNodes[city.name] = cost

	#return Boolean This method will return whether a given city can be reached from this node
	#Node city is the unique name of the city
	def canReach(self, city):
		return city.name in self.reachableNodes

	#return Boolean This will return whether the cost is enough to reach the given city
	#Node city is the unique name of the city
	#int money is the money given to reach the city
	def canReachWith(self, city, money):
		return (self.canReach(city) and self.reachableNodes[city.name] <= money)
	
	#return void This will increment the cost to occupy the next spot
	#int player isthe unique name of the player
	def addPlayer(self, player):
		if (self.currentCost > 20 or self.playerHere(player)):
			raise Exception("The player is already in " + self.name)
		if (self.currentCost < 20):
			self.currentCost += 5
		self.occupiedPlayers.append(player)

	#return Boolean This method will return whether a given player is in this city
	#int player The unique name of the player
	def playerHere(self, player):
		return (self.occupiedPlayers.count(player) != 0)
		
	#return int This method will return the cost to reach a given city, and None if the city is not in reachable
	#Node city is the unique name of the city to reach
	def getCost(self, city):
		return self.reachableNodes.get(city.name)
	
	#return int This method will return the cost to rent this place
	def getRent(self):
		return self.currentCost

