#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a custom widget.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
import PySide.QtGui
import PySide.QtCore


class Communicate(PySide.QtCore.QObject):
    
    updateBW = PySide.QtCore.Signal(int)


class BurningWidget(PySide.QtGui.QWidget):
  
    def __init__(self):      
        super(BurningWidget, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]


    def setValue(self, value):

        self.value = value


    def paintEvent(self, e):
      
        qp = PySide.QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
      
    def drawWidget(self, qp):
      
        font = PySide.QtGui.QFont('Serif', 7, PySide.QtGui.QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10.0))

        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))

        if self.value >= 700:
        
            qp.setPen(PySide.QtGui.QColor(255, 255, 255))
            qp.setBrush(PySide.QtGui.QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(PySide.QtGui.QColor(255, 175, 175))
            qp.setBrush(PySide.QtGui.QColor(255, 175, 175))
            qp.drawRect(full, 0, till-full, h)
            
        else:
            qp.setPen(PySide.QtGui.QColor(255, 255, 255))
            qp.setBrush(PySide.QtGui.QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)


        pen = PySide.QtGui.QPen(PySide.QtGui.QColor(20, 20, 20), 1, 
            PySide.QtCore.Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(PySide.QtCore.Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)

        j = 0

        for i in range(step, 10*step, step):
          
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i-fw/2, h/2, str(self.num[j]))
            j = j + 1
            

class Example(PySide.QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        sld = PySide.QtGui.QSlider(PySide.QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(PySide.QtCore.Qt.NoFocus)
        sld.setRange(1, 750)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()        
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)
        hbox = PySide.QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = PySide.QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()
        
    def changeValue(self, value):
             
        self.c.updateBW.emit(value)        
        self.wid.repaint()
        
        
def main():
    
    app = PySide.QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
