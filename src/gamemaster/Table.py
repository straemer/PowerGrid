import Deck
import PowerPlant

STAGE3 = "STAGE3"

class Table(object):
    def __init__(self):
        # create the Deck
        self.deck = Deck.Deck()
        # create the cards on the Table
        self.cardsOnTable = []
        for i in range(0,8):
            self.addPowerPlant()
       
    def __removeCard(self, cardToFind):
        for (i,card) in enumerate(self.cardsOnTable):
            if card.cost == cardToFind or  card.type == cardToFind:
                return self.cardsOnTable.pop(i)

        print("Invalid Card. Could not locate")
        
    def removePowerPlant(self, card):
        card =  self.__removeCard(card)
        self.cardsOnTable.append(self.deck.drawCard())
        return card
    
    
    def addPowerPlant(self):
        self.cardsOnTable.append(self.deck.drawCard())

table = Table()
print (table.deck.placeCardOnTop("STAGE3"))
card = table.removePowerPlant(3)
print (card)