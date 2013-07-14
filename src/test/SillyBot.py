#!/usr/bin/python3

# File SillyBot.py
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
import sys
sys.path.append('../..')

from src.ServerRequestTypes import *

def print_helper(responseNum, responseText):
    print("RESPONSE\n" + str(responseNum) + responseText + "\nEND")
    sys.stdout.flush()

def run():
    bid = 0
    for line in sys.stdin:
        parsedRequest = []
        if line.lower() == "request\n":
            responseNum = sys.stdin.readline() # get request number
            requestType = sys.stdin.readline() # get request type
            for line in sys.stdin:
                if line.lower() == "end\n":
                     break
                parsedRequest.append(line)
            if int(requestType) == ServerRequestTypes.AUCTION_START:
                print_helper(responseNum, str(10))
            elif int(requestType) == ServerRequestTypes.POWER_PLANT_BID:
                print_helper(responseNum, str(bid))
                bid = bid + 1
            elif int(requestType) == ServerRequestTypes.RESOURCE_PURCHASE:
                purchaseResponse = "Oil 10\nCoal 5\nUranium 9001"
                print_helper(responseNum, purchaseResponse)
            elif int(requestType) == ServerRequestTypes.CITY_PURCHASE:
                cityResponse = "1 2 3\n2 3 4\n3 5 6\n4 10 12\n5 1"
                print_helper(responseNum, cityResponse)
            elif int(requestType) == ServerRequestTypes.SUPPLY_POWER_FOR_CITIES:
                powerPlantResponse = "7\n1\n2\n3\n4\n5"
                print_helper(responseNum, powerPlantResponse)
            else:
                pass

run()
