import Deck

class AuctionException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
class Auction(object):
    def __init__(self, deck, cardsOnTable):
        if (len(cardsOnTable) != 8):
            raise AuctionException("Auction must begin with 8 cards on the table")
