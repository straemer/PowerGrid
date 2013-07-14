# File ClientInputHandler.py
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

import threading

from src.server.ResponseParser import *
from src.server.RequestParser import *

class ClientInputHandler(threading.Thread):
    def __init__(self, processHandler):
        threading.Thread.__init__(self)
        self.client = processHandler.client
        self.responseParser = ResponseParser(processHandler)
    def __getFullMessage(self):
        ret = ''
        for line in self.client.stdout:
            line = line.decode('UTF-8')
            if line.lower() != 'end\n':
                ret +=line
            else:
                return ret

    def run(self):
        for line in self.client.stdout:
            line = line.decode('UTF-8')
            if line.lower() == 'request\n':
                parseRequest(self.__getFullMessage())
            elif line.lower() == 'response\n':
                self.responseParser.parse(self.__getFullMessage())
