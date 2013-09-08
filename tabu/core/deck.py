#-------------------------------------------------------------------------------
# Copyright (c) 2013 "Matteo Martelli".
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v2.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     "Matteo Martelli" - initial API and implementation
#-------------------------------------------------------------------------------

import random

class Deck(object):
    '''
    classdocs
    '''


    def __init__(self, path, startIdx):
        '''
        Constructor
        '''
        'Open the file from the given path'
        self.deckfile = open(path)
        
        '''Load the entire deck in ram 
        TODO: change this reading a JSON or XML file directly '''
        self.cards = self.deckfile.readlines()
        self.deckfile.close()
        self.currentIdx = startIdx
        
        'Store the cards that has been played'
        self.playedCards = []
    
    def getLength(self):
        return len(self.cards) 
    
    def getCard(self, targetIdx):
        '''
        Pick a card from the deck according to the given index.
        The picked card will be removed from the deck. 
        '''
        self.currentIdx = targetIdx
        card = Card(self.cards[targetIdx])
        del self.cards[targetIdx]
        self.playedCards.append(card)
        return card
        
    def getRandomCard(self):
        '''
        Pick a card randomly. The picked card will be removed from the deck.
        '''
        random.seed()
        idx = random.randrange(len(self.cards))
        return self.getCard(idx)
        
class Card(object):
    '''
    classdocs
    '''
    
    def __init__(self, words):
        '''
        Constructor
        '''
        self.goal = words.split(':')[0]
        self.tabus = words[len(self.goal)+1:].split(';')

    def getGoal(self):
        return self.goal
    
    def getTabus(self):
        return self.tabus
    
    