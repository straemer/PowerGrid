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

    def __del__(self):
        self.client.terminate()

    def __generateRequest(self, requestType, args=None):
        self.requestCount += 1
        requestText = str(requestType)
        self.requests[requestCount] = requestType
        if args != None:
            requestText += '\n' + args
        self.client.write('REQUEST\n' + str(requestCount) + '\n' + requestText + '\nEND\n')

    def requestAuctionStart(self):
        return __generateRequest(ServerRequestTypes.AuctionStart)

    def requestBid(self, powerPlant):
        return __generateRequest(ServerRequestTypes.PowerPlantBid, args=powerPlant.toString())

    def requestMaterialPurchase(self):
        return __generateRequest(ServerRequestTypes.ResourcePurchase)

    def requestCityPurchase(self):
        return __generateRequest(ServerRequestTypes.CityPurchase)

    def requestSupplyPowerForCities(self):
        return __generateRequest(ServerRequestTypes.SupplyPowerForCities)

    def getRequestType(self, requestId):
        return self.requests[requestId]
