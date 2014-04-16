import PySide.QtCore
import PySide.QtGui
import sys
import time

#-------------------------------#
#   class for Sensor Window     #
#-------------------------------#
#                               #
#                               #
#                               #
#-------------------------------#
class SensorWindow(PySide.QtGui.QMainWindow):
   
    def __init__(self):
        PySide.QtGui.QMainWindow.__init__(self)

        self.MainWidget = PySide.QtGui.QWidget(self)
        
        direc = PySide.QtGui.QBoxLayout.LeftToRight
        layout = PySide.QtGui.QBoxLayout(direc)

        self.MainWidget.setLayout(layout)

        self.setWindowTitle('Sensor Command')
        self.setCentralWidget(self.MainWidget)


    def run(self, app):
        self.show()
        app.exec_()

