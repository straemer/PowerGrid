# File RequestParser.py
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

import re

from src.ClientRequestTypes import *

def parseRequest(request):
    splitRequest = re.split('\n', request)
    if int(splitRequest[0]) == ClientRequestTypes.PLAYER_FUNDS:
        pass
    elif int(splitRequest[0]) == ClientRequestTypes.GRAPH:
        pass
    elif int(splitRequest[0]) == ClientRequestTypes.AVAILABLE_RESOURCES:
        pass
    elif int(splitRequest[0]) == ClientRequestTypes.AVAILABLE_POWER_PLANTS:
        pass
    elif int(splitRequest[0]) == ClientRequestTypes.POWER_PLANT_PROPERTIES:
        pass
    elif int(splitRequest[0]) == ClientRequestTypes.NODE_INFO:
        pass
    elif int(splitRequest[0]) == ClientRequestTypes.ALL_POWER_PLANTS:
        pass
    elif int(splitRequest[0]) == ClientRequestTypes.PLAYSER_IN_ORDER:
        pass
    elif int(splitRequest[0]) == ClientRequestTypes.PLAYER_RESOURCES:
        pass
    elif int(splitRequest[0]) == ClientRequestTypes.CURRENT_STAGE:
        pass
    else:
        raise("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
