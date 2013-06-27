#!/usr/bin/python3

def main():
    numPlayers = 0
    while numPlayers < 2 or numPlayers > 6:
        numPlayers = int(input('Enter number of players (2-6)\n'))

if __name__ == '__main__':
    main()
