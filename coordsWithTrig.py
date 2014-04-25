import sys
import math
from PySide import QtGui, QtCore

class DrawImage(QtGui.QWidget): 
    def __init__(self, parent=None):
        super(DrawImage, self).__init__(parent)

        grid = QtGui.QHBoxLayout(self)

        filename = sys.argv[1]  
        pixmap = QtGui.QPixmap(filename)

        label = QtGui.QLabel(self)
        label.setPixmap(pixmap)

        grid.addWidget(label)
        self.setLayout(grid)

        self.setGeometry(300, 30, 800, 800)
        self.setWindowTitle("Heading Finder")
        self.show()

        #pixmap.mousePressEvent = self.arrowSelect


        self.setWindowTitle('Select Window')
        self.local_image = QtGui.QImage(filename)

        self.local_grview = QtGui.QGraphicsView()
        #self.setCentralWidget( self.local_grview )

        self.local_scene = QtGui.QGraphicsScene()

        self.image_format = self.local_image.format()
        self.pixMapItem = self.local_scene.addPixmap( QtGui.QPixmap(self.local_image) )
        self.pixMapItem = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(self.local_image), None, self.local_scene)

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

    def arrowSelect( self, event ):
        print 'Click the root of the arrow'
        positionBase = QtGui.QPoint( event.pos().x(), event.pos().y())
        if positionBase:
            print 'Click the tip of the arrow'
            positionTip = QtGui.QPoint( event.pos().x(), event.pos().y())
        if positionTip:
            #set in 4 quadrant system then set base as origin and tip relative to base
            imageHeight = 540
            imageWidth = 960
            point0 = QPoint(positionBase.x()-imageWidth/2, imageHeight/2 - positionBase.y())
            point1 = QPoint(positionTip.x()-imageWidth/2 - point0.x(), imageHeight/2 - positionTip.y() - point0.y())
            point0.setX(0)
            point0.setY(0)
            h = math.hypot(point1.x(),point1.y());
            theta = math.asin(point1.y()/h) * 180/math.pi
            #find which quad tip is in and adjust theta accordingly
            if point1.x() == 0 & point1.y() == 0:
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
        headingArrow = 45 + theta
        return headingArrow 
        

def main():
    app = QtGui.QApplication(sys.argv)
    form = DrawImage()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
