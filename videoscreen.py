# GUI Window for streaming video from aircraft
import sys
import msvcrt as m
import subprocess

from PySide import QtCore, QtGui 
import coordsWithTrig
filecount = 0
## Class to define frame layout
#
# class Communicate(PySide.QtCore.QObject):
# 	sendUpdate = Pyside.QtCore.Signal(str)

class ControlCenter(QtGui.QWidget):
	def __init__(self):
		super(ControlCenter, self).__init__()
		self.createButtonsLayout()
		grid = QtGui.QVBoxLayout()
		
		self.setLayout(grid)

		# self.image = QtGui.QImage(300, 300, QtGui.QImage.Format_ARGB32)
		# initial_color = QtGui.qRgb(189, 149, 39)
		# self.image.fill(QtGui.qRgb(255, 0, 0))
		# image_label = QtGui.QLabel(" ")
		# image_label.setPixmap(QtGui.QPixmap.fromImage(self.image))
		# grid.addWidget(image_label)
		grid.addLayout(self.buttonsLayout)
		# self.c1 = Communicate()
		# self.c1.sendUpdate[str].connect(self.sendFilename)

		self.setGeometry(300, 300, 200, 100) # 1920, 700, 200, 200
		self.setWindowTitle('SEC GCS')
		self.show()

## Screenshot capabilities

	def screenCaptureWidget(self): 
		fileformat = "png"
		global filecount
		filename = "/Screenshot"	
		altname = "Screenshot"	
		readfile = altname + str(filecount) + "." + fileformat

		pixmap =  QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId(), 500, 500, 1000, 1000) # 1920, 0, 960, 540
		initialPath = QtCore.QDir.currentPath() + filename + str(filecount) + "." + fileformat 
		filename = initialPath

		pixmap.save(filename, fileformat)
		filecount += 1
		path = QtCore.QDir.currentPath()
		cmd = [path + '/' + 'coordsWithTrig.py' , readfile]
		print path
		print readfile
		process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
		# for line in process.stdout:
		# 		print(line)
		#self.image.load(filename)
		# self.sendFilename(filename)

	def createButtonsLayout(self):
		self.saveScreenshotButton = self.createButton("Save Screenshot", self.screenCaptureWidget)
		self.buttonsLayout = QtGui.QHBoxLayout()
		self.buttonsLayout.addWidget(self.saveScreenshotButton)

	def createButton(self, text, member):
		button = QtGui.QPushButton(text)
		button.clicked.connect(member)
		return button

	# def sendFilename(self, filename):
	# 	self.c1.sendUpdate.emit(filename)

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