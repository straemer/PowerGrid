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

class ClientInputHandler:
    def __init__(self, client):
        self.client = client
    def __getFullMessage(self):
        ret = ''
        for line in self.client.stdin:
            if line.lower() != 'end\n':
                ret +=line
            else:
                return ret

    def run(self):
        for line in self.client.stdin:
            if line.lower() == 'request\n':
                parseRequest(__getFullMessage())
            elif line.lower() == 'response\n':
                parseResponse(__getFullMessage())
