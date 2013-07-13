import json
import random

from PowerPlant import PowerPlant

DECK = 'deck'
CARDS = 'cards'
COST = "cost"
RESOURCE_TYPES = "resourceTypes"
RESOURCES_REQUIRED = "resourcesRequired"
HOUSES_POWERED = "housesPowered"

STAGE3 = PowerPlant(0,None,0,0)

CARDS_FILE = "listOfCards.json"


class Deck(object):
    def __init__(self):
        self.cards = []
        json_data = open(CARDS_FILE)
        #strip out unnecessary JSON part
        listOfCards = json.load(json_data)[DECK][CARDS]
        json_data.close()
        for jsonElement in listOfCards:
            plant = PowerPlant(jsonElement[COST], jsonElement[RESOURCE_TYPES], jsonElement[RESOURCES_REQUIRED], jsonElement[HOUSES_POWERED])
            self.cards.append(plant)
        
        self.cards.append(STAGE3)        
        self.shuffle()
        
        #As per game play, move STAGE3 to bottom, move stage 13 to top      
        self.placeCardAtBottom("STAGE3")
        self.placeCardOnTop(13)
        
        for i in range (10,2,-1):
            self.placeCardOnTop(i)

    def __popAndMove(self, cardToFind, newIndex):
        for (i,card) in enumerate(self.cards):
            if card.cost == cardToFind or  card.type == cardToFind:
                self.cards.insert(newIndex, self.cards.pop(i))
                return
        print("Invalid Card. Could not locate")
            
    def placeCardOnTop(self, cardID):       
        self.__popAndMove(cardID,0)
            
    def placeCardAtBottom(self, cardID):
        self.__popAndMove(cardID,len(self.cards)-1)
            
    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        try:
            return self.cards.pop(0)
        except IndexError:
            #Deck has possibly ran out of cards
            print("Deck has run out of cards")  
            return None        