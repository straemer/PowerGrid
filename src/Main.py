# File Main.py
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

from src.server.ProcessHandler import ProcessHandler

def main():
    numPlayers = 0
    while numPlayers < 2 or numPlayers > 6:
        numPlayers = int(input('Enter number of players (2-6)\n'))

    processHandlers = []

    for playerNum in range(0,numPlayers):
        processHandlers.append(
            ProcessHandler(
                input('Enter process for player ' + str(playerNum) + '\n')))
