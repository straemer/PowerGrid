# File ResponseParser.py
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

import re as regex

from src.ServerRequestTypes import *

class ResponseParser:
    def __init__(self, processHandler):
        self.processHandler = processHandler

    def parse(response):
        try:
            splitResponse = regex.split('\n', response)
            requestId = splitResponse[0]
            requestType = processHandler.getRequestType(requestId)
            if int(requestType) == ServerRequestTypes.AUCTION_START:
                self.processHandler.writeResponse(int(splitResponse[1]))
            elif int(requestType) == ServerRequestTypes.POWER_PLANT_BID:
                self.processHandler.writeResponse(int(splitResponse[1]))
            elif int(requestType) == ServerRequestTypes.RESOURCE_PURCHASE:
                parsedResponse = []
                for line in splitResponse[1:]:
                    resourcePair = regex.split('\\s+', line)
                    parsedResponse.append((resourcePair[0], int(resourcePair[1])))
                self.processHandler.writeResponse(parsedResponse)
            elif int(requestType) == ServerRequestTypes.CITY_PURCHASE:
                parsedResponse = []
                for line in splitResponse[1:]:
                    cityList = regex.split('\\s+', line)
                    parsedResponse.append(cityList)
                self.processHandler.writeResponse(parsedResponse)
            elif int(requestType) == ServerRequestTypes.SUPPLY_POWER_FOR_CITIES:
                # expects first line is number of cities - the rest are power plant numbers
                parsedPowerPlants[]
                for line in splitResponse[2:]:
                     parsedPowerPlants.append(line)
                parsedResponse = (int(splitResponse[1]), parsedPowerPlants)           
                self.processHandler.writeResponse(parsedResponse)
            else:
                self.processHandler.writeResponse(None)
        except:
            self.processHandler.writeResponse(None)
