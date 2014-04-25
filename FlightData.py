#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial 

In this example, we create a bit
more complicated window layout using
the QGridLayout manager. 

author: Jan Bodnar
website: zetcode.com 
last edited: August 2011
"""

import sys
from PySide import QtGui
from PySide import QtCore
import math
#import messaging

# NameError: name 'PySide' is not defined
timer = PySide.QtCore.QTimer()
timer.timeout.connect(FlightDataStream)

class FlightData(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
    
    # Josh the following lines are from your email. not sure where this is gets placed
    def FlightDataStream(FlightData):
        d = self.zmq_handler.receive()
        for child_widget in FlightData.children():
                n = child_widget.objectName()
                if n is 'longitude':
                        FlightData.GPS_long_value(d['longitude'])
                elif n is 'latitude':
                        FlightData.GPS_lat_value(d['latitude'])
                elif n is 'altitude':
                        FlightData.altitude_value(d['altitude'])
                elif n is 'heading':
                        FlightData.heading_value(d['heading'])

    # email script ends here

        
    def initUI(self):

        # Labels in GUI
        GPSLatTitle = QtGui.QLabel('GPS LATITUDE:')
        GPSLongTitle = QtGui.QLabel('GPS LONGITUDE:')
        headingTitle = QtGui.QLabel('HEADING:')
        altitudeTitle = QtGui.QLabel('ALTITUDE:')

        # Units in GUI
        GPSLatUnits = QtGui.QLabel('degrees')
        GPSLongUnits = QtGui.QLabel('degrees')
        headingUnits = QtGui.QLabel('degrees')
        altitudeUnits = QtGui.QLabel('m')

        # Declare variable and object names
        GPSLatValue = QtGui.QLabel(GPSLat)
        GPSLatValue.setObjectName('GPS_lat_value')
        GPSLongValue = QtGui.QLabel(GPSLong)
        GPSLongValue.setObjectName('GPS_long_value')
        headingValue = QtGui.QLabel(heading)
        headingValue.setObjectName('heading_value')
        altitudeValue = QtGui.QLabel(altitude)
        altitudeValue.setObjectName('altitude_value')

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(GPSLatTitle, 1, 0)
        grid.addWidget(GPSLatValue, 1, 1)
        grid.addWidget(GPSLatUnits, 1, 2)

        grid.addWidget(GPSLongTitle, 2, 0)
        grid.addWidget(GPSLongValue, 2, 1)
        grid.addWidget(GPSLongUnits, 2, 2)

        grid.addWidget(headingTitle, 3, 0)
        grid.addWidget(headingValue, 3, 1)
        grid.addWidget(headingUnits, 3, 2)

        grid.addWidget(altitudeTitle, 4, 0)
        grid.addWidget(altitudeValue, 4, 1)
        grid.addWidget(altitudeUnits, 4, 2)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('FLIGHT DATA')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
