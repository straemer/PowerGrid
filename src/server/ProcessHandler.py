# File ProcessHandler.py
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

import subprocess
from copy import *

from src.server.ClientInputHandler import *
from src.ServerRequestTypes import *

class ProcessHandler:
    def __init__(self, processName):
        self.client = subprocess.Popen(processName,
                                       stdin = subprocess.PIPE,
                                       stdout = subprocess.PIPE)
        self.requestCount = 0
        self.inputHandler = ClientInputHandler(self)
        self.inputHandler.start()
        self.requests = {}
        self.__condition = threading.Condition()
        self.__responseLock = threading.Lock()
        self.__response = None

    def __del__(self):
        self.client.terminate()

    def __generateRequest(self, requestType, args=None):
        self.requestCount += 1
        requestText = str(requestType)
        self.requests[requestCount] = requestType
        if args != None:
            for arg in args:
                requestText += '\n' + arg
        self.__condition.acquire()
        self.client.write('REQUEST\n' + str(requestCount) + '\n' + requestText + '\nEND\n')
        self.__condition.wait()
        self.__responseLock.acquire()
        ret = copy(self.response)
        self.__responseLock.release()
        return ret

    #@return int representing PowerPlant to begin bidding on
    def requestAuctionStart(self):
        return __generateRequest(ServerRequestTypes.AuctionStart)

    #@param player - player that currently has highest bid
    #@return int representing Price player bid
    def requestBid(self, powerPlant, minBid, player):
        return __generateRequest(ServerRequestTypes.PowerPlantBid,
                                 args=[powerPlant.toString(), str(minBid), str(player)])

    def requestMaterialPurchase(self):
        return __generateRequest(ServerRequestTypes.ResourcePurchase)

    def requestCityPurchase(self):
        return __generateRequest(ServerRequestTypes.CityPurchase)

    def requestSupplyPowerForCities(self):
        return __generateRequest(ServerRequestTypes.SupplyPowerForCities)

    def getRequestType(self, requestId):
        return self.requests[requestId]

    def writeResponse(self, response):
        self.__condition.acquire()
        self.__responseLock.acquire()
        self.__response = response
        self.__responseLock.release()
        self.__condition.notify()
        self.__condition.release()
