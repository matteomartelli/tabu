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
from datetime import datetime

class Turn(object):
    
    '''
    This class refers to a team "turn" in the game. 
    Before a team starts to play (after a team switch too), 
    a "turn" object related to that team should be created. 
    All the "turn" related functionalities are handled by this class.    
    '''
    
    def __init__(self, game, team, timeout):
        '''
        Constructor
        '''
        self.game = game
        self.team = team
        self.score = 0
        self.discardedCards = 0
        self.timeout = timeout
        self.running = False
        self.paused = False
        
    def incrementScore(self): 
        self.score += 1
    
    def decrementScore(self):
        self.score -= 1
        
    def getScore(self):
        return self.score
    
    def setScore(self, score):
        self.score = score
    
    def incrementDiscardedCards(self):
        self.discardedCards += 1
    
    def decrementDiscardedCards(self):
        self.discardedCards -= 1 
    
    def getDiscardedCards(self):
        return self.discardedCards
    
    def setDiscardedCards(self, value):
        self.discardedCards = value
    
    def getTimeout(self):
        return self.timeout
    
    def getTeam(self):
        return self.team
    
    def start(self):
        '''
        Set the team current "turn" as started.
        '''
        self.running = True
        if self.paused == True:
            self.paused = False
        self.startTime = datetime.now()
    
    def pause(self):
        '''
        Pause the turn.
        '''
        if self.running == True or self.paused == False:
            self.paused = True
            self.running = False
        else:
            raise Exception("Can't pause a non running turn or a already paused turn")
    
    def stop(self):
        '''
        End the team current "turn".
        '''
        self.running = False
        self.paused = False
        
    def isRunning(self):
        return self.running
    
    def isPaused(self):
        return self.paused    
        