# File ResponseParser.py
# This file is a part of PowerGrid
# Copyright 2013 Stephen Kraemer

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

import re #regex

from src.ServerRequestTypes import *

class ResponseParser:
    def __init__(self, processHandler):
        self.processHandler = processHandler

    def parse(response):
        splitResponse = re.split('\n', response)
        requestId = splitResponse[0]
        requestType = processHandler.getRequestType(requestId)
        if int(requestType) == ServerRequestTypes.AuctionStart:
            pass
        elif int(requestType) == ServerRequestTypes.PowerPlantBid:
            pass
        elif int(requestType) == ServerRequestTypes.ResourcePurchase:
            pass
        elif int(requestType) == ServerRequestTypes.CityPurchase:
            pass
        elif int(requestType) == ServerRequestTypes.SupplyPowerForCities:
            pass
        else:
            pass
