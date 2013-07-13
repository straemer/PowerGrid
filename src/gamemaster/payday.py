#Power Grid Payday
#Used to pay the players at the beginning of the turn
class Payday:
	def __init__(self):
		self.payScheme = {0 :10, 1 : 22, 2:33,
											3:44, 4:54, 5:64, 6:73,
											7:82, 8:90, 9:98, 10:105,
											11:112, 12:118, 13:124, 
											14:129, 15:134, 16:138,
											17:142, 18:145, 19:148, 
											20:150 }
	
	#return int This method will return the amount paid to the player
	#int cities The number of powered cities the player has
	def pay(self, cities):
		return self.payScheme.get(cities)
