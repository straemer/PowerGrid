#Power Grid Gamemaster
#Will manage the game and each step
import payday
import Table
import Resource
import Auction
import player
from random import shuffle

class Game:
	NOT_ENOUGH_RESOURCES = "Not enough resources available"
	NOT_ENOUGH_MONEY = "Player does not have enough money"
	def __init__(self, numPlayers):
		self.currentPhase = 1
		self.gameover = False
		self.numPlayers = numPlayers 
		self.Table = Table.Table()
		self.PHASEMAP = {2: 10, 3: 7, 4:7, 5:5, 6:6 }
		self.GAMEEND = {2:21, 3:17, 4:17, 5:15, 6:14}
		self.players = []
		for i in range(2, numPlayers):
			newPlayer = player.Player()
			newPlayer.addMoney(50)
			self.players.append(newPlayer)
		self.ResourceMarket = Resource.Resource(numPlayers)
		
		# Initializes player turns when game starts
	def initializePlayerTurns(self):
		return shuffle(self.players)

	#return Array[Player] This method will return an arrray of players
	#in the order they will play
	#Array[Player] players all the players currently in the game
	def calculateTurns(self):
		return	sorted(self.players, key = lambda player: 
												(player.cities + float(player.highest)/10))

	def checkAdvancePhaseTwo(self):
		#Calculate which phase we are in
		maxCities = -1
		for player in self.players:
			if (player.get_cities() > maxCities):
				maxCities = player.get_cities()
		if (self.PHASEMAP[self.numPlayers] <= maxCities):
			self.currentPhase = 2
			self.ResourceMarket.update_game_phase(self.currentPhase)	

	#availableCards the cards that are up for auction
	def checkAdvancePhaseThree(self, availableCards):
		deck = self.Table.getDeck()
		if ((deck.STAGE3 in availableCards) and self.currentPhase == 2):
			self.currentPhase = 3
			self.ResourceMarket.update_game_phase(self.currentPhase)	



	def main(self):

		#TODO Load the map blocked need map object

		#init turns
		#TODO
		self.initializePlayerTurns()
		for player in reversed(self.players):
			while (len(player.get_PowerPlants()) == 0):
				auction = Auction.Auction(self.Table.getDeck(), 
																			self.Table.getCardsForAuction() + self.Table.getFutureCardsForAuction())
				#TODO Anandh add auction stuff

		while (not self.gameover):
			print ("buy resources")
			#PHASE 2 bid for resources
			for player in self.players:
				request = {}
				request[Resource.COAL] = player.getCoalRequest() 
				request[Resource.OIL] = player.getOilRequest()
				request[Resource.GARBAGE] = player.getGarbageRequest()
				request[Resource.URANIUM] = player.getUraniumRequest()
				cost = Resource.buy_resource(request)
				if (cost == 0):
					player.warn(NOT_ENOUGH_RESOURCES)
				elif (cost <= player.f_b_get_money()):
					player.pay(cost)
					player.add_coal(request[Resource.COAL])
					player.add_oil(request[Resource.OIL])
					player.add_garbage(request[Resource.GARBAGE])
					player.add_uranium(request[Resource.URANIUM])
				else: 
					#This case there is not enough money
					player.warn(NOT_ENOUGH_MONEY)
			self.ResourceMarket.restore_resources()
			
				

			#PHASE 3 buy cities
			#TODO Blocked no map available

			#PHASE 4 power cities
			for player in self.players:
				player.powerCities()
			#TODO check game end 

			#PHASE 5 pay the players
			for player in self.players:
				player.addMoney(payday.pay(player.get_cities_powered))
			
			#Check if advance to 2
			if (self.currentPhase == 1):
				self.checkAdvancePhaseTwo()

			for player in self.players:
				if (player.get_cities() >= self.GAMEEND[self.numPlayers]):
					self.gameover = True
			#PHASE 1 bid for power plants
			self.players = calculateTurns()
			availableCards = self.Table.getCardsForAuction()
			futureCards = self.Table.getFutureCardsForAuction()
			self.checkAdvancePhaseThree(availableCards)
			#Pass to players
			#TODO Auction
			print ("Bid for power plants")
			auction = Auction.Auction(self.Table.getDeck(), availableCards + futureCards)
			#use reversed()
Game = Game(5)
Game.main()
