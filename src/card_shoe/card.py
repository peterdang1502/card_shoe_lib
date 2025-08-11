from constants import *
from typing import *

class Card:
    def __init__(self, rank, suit):
        '''Constructor for a card'''
        self.rank = rank
        self.suit = suit
        
    def get_rank(self):
        '''Get a card's rank'''
        return self.rank
    
    def get_suit(self):
        '''Get a card's suit'''
        return self.suit

    # def is_ace(self):
    #     '''Return whether a card is an ace or not'''
    #     return self.rank == CARD_RANKS[-1]
    
    def __str__(self):
        return "% s of % s" % (self.rank, self.suit)
    
    def __repr__(self):
        return "% s of % s" % (self.rank, self.suit)
    
    # def __eq__(self, other: type[Card]):
    #     return self.get_rank() == other.get_rank()