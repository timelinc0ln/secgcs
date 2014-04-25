# GUI Window for streaming video from aircraft
import sys
import msvcrt as m

from PySide import QtCore, QtGui 

filecount = 0
## Class to define frame layout
#
class ControlCenter(QtGui.QWidget):
	def __init__(self):
		super(ControlCenter, self).__init__()
		self.createButtonsLayout()
		grid = QtGui.QVBoxLayout()
		grid.addLayout(self.buttonsLayout)		
		self.setLayout(grid)

		self.setGeometry(300, 300, 200, 200) # 1920, 700, 200, 200
		self.setWindowTitle('Video Stream')
		self.show()

## Screenshot capabilities

	def screenCaptureWidget(self): 
		filename = "/Screenshot"
		global filecount
		fileformat = "png"
		pixmap =  QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId(), 500, 500, 1000, 1000) # 1920, 0, 960, 540
		initialPath = QtCore.QDir.currentPath() + filename + str(filecount) + "." + fileformat 
		filename = initialPath
		pixmap.save(filename, fileformat)
		filecount += 1

	def createButtonsLayout(self):
		self.saveScreenshotButton = self.createButton("Save Screenshot", self.screenCaptureWidget)
		self.buttonsLayout = QtGui.QHBoxLayout()
		self.buttonsLayout.addWidget(self.saveScreenshotButton)

	def createButton(self, text, member):
		button = QtGui.QPushButton(text)
		button.clicked.connect(member)
		return button

class ScreenShot(QtGui.QWidget):
	def __init__(self):
		super(ScreenShot, self).__init__()
		self.initWidget(filename)

	def initWidget(self):
		hbox = QtGui.QHBoxLayout(self)
		pixmap = QtGui.QPixmap(filename)

		lbl = QtGui.QLabel(self)
		lbl.setPixmap(pixmap)

		hbox.addWidget(lbl)
		self.setLayout(hbox)

		self.setGeometry(300, 300, 1000, 600)
		self.setWindowTitle('Image viewer')
		self.show() 
		


	def pixelSelect( self, event ):
		print 'hello'
		position = QPoint( event.pos().x(),  event.pos().y())
		self.setWindowTitle( 'Pixel position = (' + str( event.pos().x() ) + ' , ' + str( event.pos().y() ))



if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = ControlCenter()
	sys.exit(app.exec_())