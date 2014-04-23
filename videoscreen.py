# GUI Window for streaming video from aircraft
import sys

from PySide import QtCore, QtGui
#from PySide.QtCore import QX11EmbedWindow
#from PySide.QtGui import QX11EmbedContainer 


class CameraDisplay(QtGui.QLabel):
	def __init__(self):
		super(CameraDisplay, self).__init__()

	def updateFrame(self, image):
		self.setPixmap(QtGui.QPixmap.fromImage(image))

filecount = 0
## Class to define frame layout
#
class ControlCenter(QtGui.QWidget):
	up_camera_signal = QtCore.Signal(QtGui.QImage)
	up_camera = None

	def __init__(self):
		super(ControlCenter, self).__init__()
		self.up_camera = CameraDisplay()
		self.up_camera_signal.connect(self.up_camera.updateFrame)

		self.createButtonsLayout()
		
		grid = QtGui.QVBoxLayout()
		#grid.setSpacing(10)

		grid.addWidget(self.up_camera, 0, 0)
		grid.addLayout(self.buttonsLayout)		

		self.setLayout(grid)

		self.setGeometry(300, 50, 1280, 920)
		self.setWindowTitle('Video Stream')
		self.show()

	## Class for getting data to display
	# TODO: Figure out how to do this...
	#
	def up_camera_callback(self, data):
		'''This function gets called by an external thread'''
		try:
		  image = QtGui.QImage(data.data, data.width, data.height, QtGui.QImage.Format_RGB888)
		  self.up_camera_signal.emit(image)

		except Exception, e:
		  print(e)

## Screenshot capabilities
	def screenCaptureWidget(widget): 
		filename = "Screenshot"
		global filecount
		fileformat = "png"
		pixmap =  QtGui.QPixmap.grabWidget(widget)
		initialPath = QtCore.QDir.currentPath() + filename + str(filecount) + "." + fileformat 
		filename = initialPath
		pixmap.save(filename, fileformat)
		filecount += 1

	def createButtonsLayout(self):
		self.saveScreenshotButton = self.createButton("Save Screenshot", self.screenCaptureWidget)
		self.buttonsLayout = QtGui.QHBoxLayout()
		#self.addStretch()
		self.buttonsLayout.addWidget(self.saveScreenshotButton)

	def createButton(self, text, member):
		button = QtGui.QPushButton(text)
		button.clicked.connect(member)
		return button

	def updateScreenshotLabel(self):
		self.screenshotLabel.setPixmap(self.originalPixmap.scaled(
			self.screenshotLabel.size(), QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation))

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = ControlCenter()
	# player = MoviePlayer()
	# player.show()
	sys.exit(app.exec_())