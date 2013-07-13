#!/usr/bin/python3

# MockGameMaster.py
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

import random
import sys
sys.path.append('../..')

from src.server.ProcessHandler import *

if __name__ == '__main__':
    processHandler = ProcessHandler('./SillyBot.py')
    randomFunctions = [processHandler.requestAuctionStart,
                       processHandler.requestBid,
                       processHandler.requestMaterialPurchase,
                       processHandler.requestCityPurchase,
                       processHandler.requestSupplyPowerForCities]
    random.seed()
    for i in range(100):
        function = randomFunctions[random.randint(0,len(randomFunctions)-1)]
        if function == processHandler.requestBid:
            minBid = random.randint(0, 9001)
            powerPlant = random.randint(0,1337)
            player = random.randint(0, 5)
            print("Response: " + str(function(minBid, powerPlant, player)))
        else:
            print("Response: " + str(function()))
