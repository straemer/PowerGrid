import Deck

class Table(object):
    def __init__(self):
        # create the Deck
        self.deck = Deck.Deck()
        # create the cards on the Table
        self.cardsOnTable = []
        self.removedCards = []
        for i in range(0, 8):
            self.addPowerPlantToAuction()
       
    def __removeCard(self, cardToFind):
        for (i, card) in enumerate(self.cardsOnTable):
            if card.cost == cardToFind or  card.type == cardToFind:
                return self.cardsOnTable.pop(i)

        print("Invalid Card. Could not locate")
      
    def getDeck(self):
    	return self.deck

    def addPowerPlantToAuction(self):
            self.cardsOnTable.append(self.deck.drawCard())
  
    def removePowerPlantFromAuction(self, cardID):
        removedCard = self.__removeCard(cardID)
        if (removedCard is None):
            return
        # Need to have always 8 cards
        replacedCard = self.deck.drawCard()
        if replacedCard.type == "STAGE3":
            # TODO: Insert Stage 3 code
            pass
        self.cardsOnTable.append(replacedCard)
        return removedCard
    
    #This method will need a power plant object, since it does not have the info just given an id anymore
    def placePowerPlantUnderDeck(self, powerplant):
        self.deck.cards.append(powerplant)
    #This method will need a power plant object, since it does not have the info just given an id anymore  
    def removePowerPlantFromPlay(self, powerplant):
        self.removedCards.append(powerplant)       
          
    def getCardsForAuction(self):
        if len(self.cardsOnTable) > 4:
            return sorted(self.cardsOnTable, key=lambda card: card.cost)[0:4]
        else :
            return self.cardsOnTable
        
    def getFutureCardsForAuction(self):
        if len(self.cardsOnTable) > 4:
            return sorted(self.cardsOnTable, key=lambda card: card.cost)[4:len(self.cardsOnTable)]
        else :
            return self.cardsOnTable
