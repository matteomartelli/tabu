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
'''
Created on Aug 30, 2013

@author: "Matteo Martelli"
'''

#Data things
__DATA_FOLDER = "../../data" #TODO Change this after handling the binaries creation
DECKS_FOLDER = __DATA_FOLDER + "/decks"
DEFAULT_TEAMS_NUMBER = 2
CARD_BLUE_PATH = __DATA_FOLDER + "/img/card_blue.svg"
CARD_RED_PATH = __DATA_FOLDER + "/img/card_red.svg"
CARD_PATHS = [CARD_BLUE_PATH, CARD_RED_PATH] #TODO: add more color
BUTTON_ICON_GUESSED = __DATA_FOLDER + "/img/button_icon_guessed.svg"
BUTTON_ICON_WRONG = __DATA_FOLDER + "/img/button_icon_wrong.svg"
BUTTON_ICON_PLAY_PAUSE = __DATA_FOLDER + "/img/button_icon_playpause.svg"
BUTTON_ICON_STOP = __DATA_FOLDER + "/img/button_icon_stop.svg"


QTIMER_INTERVAL = 1000 # 1 second interval
