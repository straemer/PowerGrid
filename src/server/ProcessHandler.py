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
import threading
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
        self.requests[self.requestCount] = requestType
        if args != None:
            for arg in args:
                requestText += '\n' + arg
        self.__condition.acquire()
        self.client.stdin.write(bytes('REQUEST\n' + str(self.requestCount) + '\n' + requestText + '\nEND\n', 'UTF-8'))
        self.__condition.wait()
        with self.__responseLock:
            return copy(self.response)

    #@return int representing PowerPlant to begin bidding on
    def requestAuctionStart(self):
        return self.__generateRequest(ServerRequestTypes.AUCTION_START)

    #@param player - player that currently has highest bid
    #@return int representing Price player bid
    def requestBid(self, powerPlant, minBid, player):
        return self.__generateRequest(ServerRequestTypes.POWER_PLANT_BID,
                                 args=[powerPlant.toString(), str(minBid), str(player)])

    def requestMaterialPurchase(self):
        return self.__generateRequest(ServerRequestTypes.RESOURCE_PURCHASE)

    def requestCityPurchase(self):
        return self.__generateRequest(ServerRequestTypes.CITY_PURCHASE)

    def requestSupplyPowerForCities(self):
        return self.__generateRequest(ServerRequestTypes.SUPPLY_POWER_FOR_CITIES)

    def getRequestType(self, requestId):
        return self.requests[requestId]

    def writeResponse(self, response):
        with self.__condition:
            with self.__responseLock:
                self.__response = response
            self.__condition.notify()
