#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows a QtGui.QSlider widget.

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""


import PySide.QtCore
import PySide.QtGui
import sys

class Example(PySide.QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        sld = PySide.QtGui.QSlider(PySide.QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(PySide.QtCore.Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        
        self.label = PySide.QtGui.QLabel(self)
        self.label.setPixmap(PySide.QtGui.QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80, 30)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QtGui.QSlider')
        self.show()
        
    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(PySide.QtGui.QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(PySide.QtGui.QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(PySide.QtGui.QPixmap('med.png'))
        else:
            self.label.setPixmap(PySide.QtGui.QPixmap('max.png'))
        
def main():
    
    app = PySide.QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
