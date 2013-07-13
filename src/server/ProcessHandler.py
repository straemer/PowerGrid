# File ProcessHandler.py
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

import subprocess

class ProcessHandler:
    def __init__(self, processName):
        self.client = subprocess.Popen(processName,
                                       stdin = subprocess.PIPE,
                                       stdout = subprocess.PIPE)
        self.requestCount = 0

    def __del__(self):
        self.client.terminate()

    def __generateRequest(self, requestString):
        self.requestCount += 1
        self.client.write('request ' + str(requestCount) + ' : ' + requestString)

    def requestAuctionStart(self):
        pass

    def requestBid(self, powerPlant):
        pass

    def requestMaterialPurchase(self):
        pass

    def requestCityPurchase(self):
        pass

    def requestPowerPowerplants(self):
        pass
