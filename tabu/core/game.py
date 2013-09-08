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
from tabu.conf.settings import DECKS_FOLDER
from deck import Deck
from team import Team
from turn import Turn

class Game(object):
    '''
    classdocs
    '''
    

    def __init__(self, lang, startPoint, nteams):
        '''
        Constructor
        '''
        # Initialize all the game related stuff 
        # TODO: error check on deckPath
        # Initialize the Deck 
        self.deckEmpty = True
        deckPath = DECKS_FOLDER + "/"+lang[0:2]+"/cards"
        self.deck = Deck(deckPath, startPoint)
        if self.deck.getLength() > 0: 
            self.deckEmpty = False
       
        # Initialize the teams object 
        self.teams = []
        for i in range(0, nteams):
            self.teams.append(Team(self, i))
        
        # Initialize the game board TODO 
        self.board = 0
    
    def newTurn(self, timeout):
        '''
        Create turn and select not last playing team.
        return back the turn object pointer.
        '''
        for t in self.teams:
            if t.wasLastPlaying() == False:
                break
        
        if t.wasLastPlaying():
            raise Exception('Error in teams switching')
        #TODO: start team play
        
        turn = Turn(self, t, timeout)
        self.currentTurn = turn
        return self.currentTurn
    
    def getCurrentTurn(self):
        return self.currentTurn
    
    def isDeckEmpty(self):
        return self.deckEmpty
    
    def getRandomCard(self):
        '''
        Pick a card randomly. The picked card will be removed from the deck.
        '''
        if self.deck.getLength() > 0:
            return self.deck.getRandomCard()
        else:
            self.deckEmpty = True
            return False
    