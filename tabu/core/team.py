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

class Team(object):
    '''
    classdocs
    '''


    def __init__(self, game, idx):
        '''
        Constructor
        '''
        self.game = game
        self.score = 0
        self.lastPlaying = False
        self.idx = idx
        
    def getIndex(self):
        return self.idx
    
    def wasLastPlaying(self):
        return self.lastPlaying
    
    def startPlay(self):
        pass
    
    def endPlay(self):
        self.lastPlaying = True