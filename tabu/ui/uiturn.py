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

from PyQt4 import QtCore, QtGui
from tabu.conf.settings import *
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

    
class TurnDialog(object):
    '''
    classdocs
    '''
    def __init__(self, game, timeout):
        self.game = game
        self.turn = self.game.newTurn(timeout)
        self.timeout = timeout
        #use the qtimer for the countdown 
        self.qtimer = QtCore.QTimer()
        self.qtimer.timeout.connect(self.updateTimer)
        idx = self.turn.getTeam().getIndex()
        self.cardImgPath = CARD_PATHS[ idx % len(CARD_PATHS) ] #TODO: the colors ant the teams number should be the same
        
    def setupUi(self, Dialog): #TODO Refactor Dialog -> dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(340, 430)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Tabu", None, QtGui.QApplication.UnicodeUTF8))
        
        #Setup Font
        self.bigFont = QtGui.QFont()
        self.bigFont = QtGui.QFont(self.bigFont.defaultFamily(), 25, self.bigFont.Bold)
        
        #Play/Pause Button Init
        self.playpauseButton = QtGui.QPushButton(Dialog)
        self.playpauseButton.setGeometry(QtCore.QRect(60, 15, 48, 48))
        self.playpauseButton.setIcon(QtGui.QIcon(BUTTON_ICON_PLAY_PAUSE))
        self.playpauseButton.setIconSize(QtCore.QSize(48, 48))
        self.playpauseButton.setObjectName(_fromUtf8("playpauseButton"))
        
        #Stop Button Init
        self.stopButton = QtGui.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(230, 15, 48, 48))
        self.stopButton.setIcon(QtGui.QIcon(BUTTON_ICON_STOP))
        self.stopButton.setIconSize(QtCore.QSize(48, 48))
        self.stopButton.setDisabled(True)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        
        #Discard Button Init
        self.discardButton = QtGui.QPushButton(Dialog)
        self.discardButton.setGeometry(QtCore.QRect(100, 380, 48, 48))
        self.discardButton.setIcon(QtGui.QIcon(BUTTON_ICON_WRONG))
        self.discardButton.setIconSize(QtCore.QSize(48,48))
        self.discardButton.setObjectName(_fromUtf8("discardButton"))
        
        #Guess Button Init
        self.guessButton = QtGui.QPushButton(Dialog)
        self.guessButton.setGeometry(QtCore.QRect(200, 380, 48, 48))
        self.guessButton.setIcon(QtGui.QIcon(BUTTON_ICON_GUESSED))
        self.guessButton.setIconSize(QtCore.QSize(48,48))
        self.guessButton.setDisabled(True)
        self.guessButton.setObjectName(_fromUtf8("guessButton"))
        
        #Discard Label Init
        self.discardLabel = QtGui.QLabel(Dialog)
        self.discardLabel.setGeometry(QtCore.QRect(60, 390, 40, 30))
        self.discardLabel.setText(_fromUtf8("0"))
        self.discardLabel.setObjectName(_fromUtf8("discardLabel"))
        self.discardLabel.setFont(self.bigFont)
        
        #Guess Label Init
        self.guessLabel = QtGui.QLabel(Dialog)
        self.guessLabel.setGeometry(QtCore.QRect(270, 390, 40, 30))
        self.guessLabel.setText(_fromUtf8("0"))
        self.guessLabel.setObjectName(_fromUtf8("guessLabel"))
        self.guessLabel.setFont(self.bigFont)
        
        #Frame Init
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(60, 70, 220, 300))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame.setStyleSheet("background-image: url("+self.cardImgPath+")")
        
        #Label Card Title Init
        self.cardTitleLabel = QtGui.QLabel(Dialog)
        self.cardTitleLabel.setGeometry(QtCore.QRect(130, 90, 90, 16))
        self.cardTitleLabel.setObjectName(_fromUtf8("cardTitleLabel"))
        
        #List View Init 
        self.listView = QtGui.QListWidget(Dialog)
        self.listView.setGeometry(QtCore.QRect(70, 160, 200, 150))
        self.listView.setFrameStyle(0)
        self.listView.setObjectName(_fromUtf8("listView"))
        
        #Label Timer Init
        self.timerLabel = QtGui.QLabel(Dialog)
        timerSize = QtCore.QSize(90, 30)
        timerLocation = QtCore.QPoint(Dialog.size().width() / 2 - (timerSize.width() / 2), 20)
        self.timerLabel.setGeometry(QtCore.QRect(timerLocation, timerSize))
        strTime = time.strftime('%M:%S', time.gmtime(self.turn.timeout))
        self.timerLabel.setText(strTime)
        self.timerLabel.setFont(self.bigFont)
        self.timerLabel.setObjectName(_fromUtf8("labelTimer"))
        
        #Connect buttons
        QtCore.QObject.connect(self.playpauseButton, QtCore.SIGNAL(_fromUtf8("clicked()")),  self.playpauseButtonClicked)
        QtCore.QObject.connect(self.stopButton, QtCore.SIGNAL(_fromUtf8("clicked()")),  self.stopButtonClicked)
        QtCore.QObject.connect(self.guessButton,  QtCore.SIGNAL(_fromUtf8("clicked()")),  self.guessButtonClicked)
        QtCore.QObject.connect(self.discardButton,  QtCore.SIGNAL(_fromUtf8("clicked()")),  self.discardButtonClicked)
        
        #Load first card
        self.loadRandomCard()
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

    def playpauseButtonClicked(self):
        if self.turn.isRunning() == False:
            self.startTurn()
        else:
            self.pauseTurn()

    def stopButtonClicked(self):
        self.stopTurn()
    
    def guessButtonClicked(self):
        self.turn.incrementScore()
        self.guessLabel.setText(str(self.turn.getScore()))
        self.loadRandomCard()

    def discardButtonClicked(self):
        self.turn.incrementDiscardedCards()
        self.discardLabel.setText(str(self.turn.getDiscardedCards()))
        self.loadRandomCard()
    
    def updateTimerLabel(self):
        strTime = time.strftime('%M:%S', time.gmtime(self.timeout))
        self.timerLabel.setText(strTime)
    
    def updateTimer(self):
        if (self.timeout > 0):
            self.timeout -= 1
            self.updateTimerLabel()
        else:
            self.stopTurn()
        
    def startTurn(self):
        self.stopButton.setDisabled(False)
        self.guessButton.setDisabled(False)
        self.turn.start()
        self.qtimer.start(QTIMER_INTERVAL)
            
    def pauseTurn(self):
        self.guessButton.setDisabled(True)
        self.turn.pause()
        self.qtimer.stop()
    
    def stopTurn(self):
        self.playpauseButton.setDisabled(True)
        self.guessButton.setDisabled(True)
        self.discardButton.setDisabled(True)
        self.stopButton.setDisabled(True)
        self.turn.stop()
        self.qtimer.stop()
        if (self.timeout > 0): self.timeout = 0
        self.updateTimerLabel()
            
    def clearCard(self):
        self.cardTitleLabel.clear()
        self.listView.clear()
    
    def loadRandomCard(self):
        self.clearCard()
        card = self.game.getRandomCard()
        if card != False:
            self.cardTitleLabel.setText(_fromUtf8(card.getGoal()))
            for tabu in card.getTabus():
                self.listView.addItem(tabu)
        elif self.game.isDeckEmpty():
            #The deck is empty
            #TODO: give more options to the user
            self.cardTitleLabel.setText("DECK ENDED")
            self.stopTurn()
            
    