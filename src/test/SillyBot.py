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

from src.server.ServerRequestTypes import *

def print_helper(responseNum, responseText):
    print("RESPONSE\n" + responseNum + "\n" + responseText + "\nEND\n")

def run():
    bid = 0
    while (True) :
        parsedRequest = []
        line = sys.stdin.readline()
        if line == "REQUEST":
            line = sys.stdin.readline() # get request number
            requestType = sys.stdin.readline() # get request type
            for line in sys.stdin:
                if line == "END"
                     break
                parsedRequest.append(line)
            if int(requestType) == ServerRequestTypes.AUCTION_START:
                self.print_helper(responseNum, 10)
            elif int(requestType) == ServerRequestTypes.POWER_PLANT_BID:
                self.print_helper(responseNum, bid)
                bid = bid + 1
            elif int(requestType) == ServerRequestTypes.RESOURCE_PURCHASE:
                purchaseResponse = "Oil 10\nCoal 5\nUranium 9001\n"
                self.print_helper(responseNum, purchaseResponse)
            elif int(requestType) == ServerRequestTypes.CITY_PURCHASE:
                cityResponse = "1 2 3\n2 3 4\n3 5 6\n4 10 12\n5 1\n"
                self.print_helper(responseNum, cityResponse)
            elif int(requestType) == ServerRequestTypes.SUPPLY_POWER_FOR_CITIES:
                powerPlantResponse = "7\n1\n2\n3\n4\n5\n"
                self.print_helper(responseNum, powerPlantResponse())
            else 
                pass
if __name__ == "__main__"
    run()
