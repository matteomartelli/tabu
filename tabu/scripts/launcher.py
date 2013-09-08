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
Created on Aug 28, 2013

@author: "Matteo Martelli"
'''
from PyQt4 import QtGui

from tabu.ui.uistart import StartForm

def run():
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QDialog()
    ui = StartForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
