import sys
import math
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import * 

class DrawImage(QMainWindow): 
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.setWindowTitle('Select Window')
        self.local_image = QImage('U:\Apps\nicetrees.png')

        self.local_grview = QGraphicsView()
        self.setCentralWidget( self.local_grview )

        self.local_scene = QGraphicsScene()

        self.image_format = self.local_image.format()
        #self.pixMapItem = self.local_scene.addPixmap( QPixmap(self.local_image) )
        self.pixMapItem = QGraphicsPixmapItem(QPixmap(self.local_image), None, self.local_scene)

        self.local_grview.setScene( self.local_scene )

        self.pixMapItem.mousePressEvent = self.pixelSelect

    def pixelSelect( self, event ):
        print 'hello'
        position = QPoint( event.pos().x(),  event.pos().y())
        color = QColor.fromRgb(self.local_image.pixel( position ) )
        if color.isValid():
            rgbColor = '('+str(color.red())+','+str(color.green())+','+str(color.blue())+','+str(color.alpha())+')'
            self.setWindowTitle( 'Pixel position = (' + str( event.pos().x() ) + ' , ' + str( event.pos().y() )+ ') - Value (R,G,B,A)= ' + rgbColor)
        else:
            self.setWindowTitle( 'Pixel position = (' + str( event.pos().x() ) + ' , ' + str( event.pos().y() )+ ') - color not valid')

    def arrowSelect( self, event, headingPlane ):
        print 'Click the root of the arrow'
        positionBase = QPoint( event.pos().x(), event.pos().y())
        if positionBase:
            print 'Click the tip of the arrow'
            positionTip = QPoint( event.pos().x(), event.pos().y())
        if positionTip:
            #set in 4 quadrant system then set base as origin and tip relative to base
            imageHeight = 540
            imageWidth = 960
            point0 = QPoint(positionBase.x()-imageWidth/2, imageHeight/2 - positionBase.y())
            point1 = QPoint(positionTip.x()-imageWidth/2 - point0.x(), imageHeight/2 - positionTip.y() - point0.y())
            point0.x() = 0
            point0.y() = 0
            h = math.hypot(point1.x(),point1.y());
            theta = math.asin(point1.y()/h) * 180/math.pi
            #find which quad tip is in and adjust theta accordingly
            if point1.x() == 0 && point1.y() ==0:
                print 'Im not even mad, but ERROR'
            if point1.x() > 0:
                if point1.y() > 0:  #quadrant 1
                    theta = 90 - theta
                else:               #quadrant 2
                    theta = 90 + theta
            else:
                if point1.y() < 0:  #quadrant 3
                    theta = 270 - theta
                else:               #quadrant 4
                    theta = 270 + theta
           return headingArrow = headingPlane + theta 
        

def main():
    app = QtGui.QApplication(sys.argv)
    form = DrawImage()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
