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
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
from tabu.core.game import Game
from tabu.ui.uiturn import TurnDialog
from tabu.conf.settings import DEFAULT_TEAMS_NUMBER


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class StartForm(object):
    def __init__(self):
        pass
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(265, 321)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Tabu Start Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_lang = QtGui.QLabel(Form)
        self.label_lang.setGeometry(QtCore.QRect(60, 30, 141, 16))
        self.label_lang.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_lang.setAutoFillBackground(False)
        self.label_lang.setText(QtGui.QApplication.translate("Form", "Choose A Language", None, QtGui.QApplication.UnicodeUTF8))
        self.label_lang.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lang.setObjectName(_fromUtf8("label_lang"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(50, 60, 161, 61))
        self.listWidget.setViewMode(QtGui.QListView.ListMode)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "English", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Espanol", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Italiano", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        self.label_card_start = QtGui.QLabel(Form)
        self.label_card_start.setGeometry(QtCore.QRect(40, 160, 121, 16))
        self.label_card_start.setText(QtGui.QApplication.translate("Form", "Start From Card", None, QtGui.QApplication.UnicodeUTF8))
        self.label_card_start.setObjectName(_fromUtf8("label_card_start"))
        self.spinBox_card = QtGui.QSpinBox(Form)
        self.spinBox_card.setGeometry(QtCore.QRect(170, 150, 59, 27))
        self.spinBox_card.setMaximum(5000)
        self.spinBox_card.setObjectName(_fromUtf8("spinBox_card"))
        self.label_time = QtGui.QLabel(Form)
        self.label_time.setGeometry(QtCore.QRect(40, 190, 131, 16))
        self.label_time.setText(QtGui.QApplication.translate("Form", "Default Time (sec)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_time.setObjectName(_fromUtf8("label_time"))
        self.spinBox_time = QtGui.QSpinBox(Form)
        self.spinBox_time.setGeometry(QtCore.QRect(170, 180, 59, 27))
        self.spinBox_time.setMinimum(0)
        self.spinBox_time.setProperty("value", 60)
        self.spinBox_time.setObjectName(_fromUtf8("spinBox_time"))
        self.pushButton_start = QtGui.QPushButton(Form)
        self.pushButton_start.setGeometry(QtCore.QRect(90, 260, 97, 27))
        self.pushButton_start.setText(QtGui.QApplication.translate("Form", "Start Game", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        QtCore.QObject.connect(self.pushButton_start,  QtCore.SIGNAL(_fromUtf8("clicked()")),  self.on_pushButton_start_clicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    #Start the main dialog
    def on_pushButton_start_clicked(self):
        lang = self.listWidget.currentItem().text().toLower()
        #Initialize the game object
        self.game = Game(lang, 0, DEFAULT_TEAMS_NUMBER)
        
        
        qtDialog = QtGui.QDialog()
        ui = TurnDialog(self.game, self.spinBox_time.value())
        ui.setupUi(qtDialog) 
        #ui.loadCard(deck.gotoCard(deck.currentIndex))
        #ui.startTimer()
        qtDialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        exit(qtDialog.exec_())
        
        
    def retranslateUi(self, Form):
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
    
    

