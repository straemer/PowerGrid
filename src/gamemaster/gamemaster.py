#Power Grid Gamemaster
#Will manage the game and each step
import payday
import Deck
import Resource

from random import shuffle

# Initializes player turns when game starts
def initializePlayerTurns(players):
  return shuffle(players)

#return Array[Player] This method will return an arrray of players
#in the order they will play
#Array[Player] players all the players currently in the game
def calculateTurns(players):
	return	sorted(players, key = lambda player: 
											(player.cities + float(player.highest)/10))
	
def main(players):
	currentPhase = 1
	players = players
	gameover = False
	DECK = Deck.Deck()
	ResourceMarket = Resource.Resource(len(players))

	#Add Players
	#Load Map
	while (not gameover):
		print ("Paying the players")
		for player in players:
			player.addMoney(payday.pay(player.get_cities_powered))

		print ("Decide the new turn order")
		players = calculateTurns(players)
		print ("Bid for power plants")


		print ("buy resources")
		ResourceMarket.update_game_phase(currentPhase)	
		for player in players:
			#for key, value in ResourceMarket.show_resources()
				#Server.updateResources(key, value)
			# Poll server for player action
			#request = {}
			#request[Resource.COAL] = 
			#request[Resource.OIL] = 
			#request[Resource.GARBAGE] =
			#request[Resource.URANIUM] = 
			cost = Resource.buy_resource(request)
			if (cost == 0):
				print ("Server.warn(not enough)")
			elif (cost <= player.f_b_get_money()):
				player.pay(cost)
				player.add_coal(request[Resource.COAL])
				player.add_oil(request[Resource.OIL])
				player.add_garbage(request[Resource.GARBAGE])
				player.add_uranium(request[Resource.URANIUM])
			else: 
				#This case there is not enough money
				print ("Server.warn(not enough money for player)")
		
			

		print ("power cities")
		#for player in players:
			#Server.poll how many you wanna power
			
		
