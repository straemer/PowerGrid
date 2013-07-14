# ServerRequestHandler.py
# This file is a part of PowerGrid
# Copyright 2013 Stephen Kraemer, Nikolai Semenenko

# PowerGrid is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# PowerGrid is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with PowerGrid.  If not, see <http://www.gnu.org/licenses/>.

import player
class ServerRequestHandler:
	def __init__(self, game):
		self.game = game

	#return int 
	def moneyRequest(self, playerId):
		for player in self.game.players:
			if (playerId == player.get_playerID()):
				return player.f_b_get_money()
	
	#TODO map is yet to be implemented in game
	def graphRequest():
		pass

	#return MAP<Resource.ENUM, int)
	def resourcesAvailable(self):
		return self.game.ResourceMarket.get_resources_on_board()

	#return Array[PowerPLant]
	def powerPlantsAvailable(self):
		return self.game.Table.getCardsForAuction() + self.game.Table.getFutureCardsForAuction()

	#TODO not sure what you are expecting here
	def getPowerPlantInfo(powerPlantId):
			pass

	#TODO not sure what info you want here either and in what format
	def getNodeInfo(nodeId):
			pass
	
	#return Array[PowerPlant]
	def getPlayerPowerPlants(self,playerId):
		for player in self.game.players:
			if (playerId == player.get_playerID()):
				return player.get_PowerPlants()

	#return Array[Players]
	def getPlayersInOrder(self):
		return self.game.players

	#return Array[int]
	def getPlayerResources(self, playerID):
		for player in self.game.players:
			if (playerID == player.get_playerID()):
				return player.getResources()

	#return int the current stage
	def getStage():
		return self.game.currentPhase
