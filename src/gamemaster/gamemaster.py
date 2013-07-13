#Power Grid Gamemaster
#Will manage the game and each step
import payday

#return Array[Player] This method will return an arrray of players
#in the order they will play
#Array[Player] players all the players currently in the game
def calculateTurns(players):
	return	sorted(players, key = lambda player: 
											(player.cities + float(player.highest)/10))
	
def main():
	currentPhase = 1
	players = []
	gameover = False

	#Add Players
	#Load Map
	while (not gameover):
		print "Pay the players"
		print "Decide the new turn order"
		calculateTurns(players)
		print "Bid for power plants"
		print "buy resources"
		print "power cities"
		
class Player:
	def __init__(self, cities, highest):
		self.cities = cities
		self.highest = highest
	
	def highestPlant(self):
		return self.highest


player1 = Player(1,10)
player2 = Player(1,33)

for player in calculateTurns([player1, player2]):
	print player.highest
