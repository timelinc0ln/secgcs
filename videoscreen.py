# GUI Window for streaming video from aircraft
import sys

from PySide import QtCore, QtGui
#from PySide.QtCore import QX11EmbedWindow
#from PySide.QtGui import QX11EmbedContainer 

## VideoStream class
# Wrote this one to test window
#
class VideoStream(QtGui, QWidget):
	def __init__(self, parent=None):
		super(VideoStream, self).__init__(parent)

		self.video = QtGui.QMovie(self)
		self.video.setCacheMode(QtGui.QMovie.CacheAll)

		self.vidoeLabel = QtGui.QLabel("No video streaming")
		self.vidoeLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.videoLabel.setSizePolicy(QtGui..QSizePolicy.Igonored, QtGui.QSizePolicy.Igonored)
		self.videoLabel.setBackgroundRole(QtGui.QPallette.Dark)
		self.videoLabel.setAutoFillBackGround(True)

## Example video display class that I found online
# Does not use QX11EmbedWidget or QX11EmbedContainer
#
class CameraDisplay(QtGui.QLabel):
	def __init__(self):
		super(CameraDisplay, self).__init__()

	def updateFrame(self, image):
		self.setPixmap(QtGui.QPixmap.fromImage(image))


## Class to define frame layout
#
class ControlCenter(QtGui.QWidget):
	up_camera_signal = QtCore.Signal(QtGui.QImage)
	up_camera = None

	def __init__(self):
		super(ControlCenter, self).__init__()
		self.up_camera = CameraDisplay()
		self.up_camera_signal.connect(self.up_camera.updateFrame)

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(self.up_camera, 0, 0)

		self.setLayout(grid)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Control Center')
		self.show()

	def up_camera_callback(self, data):
		'''This function gets called by an external thread'''
		try:
		  image = QtGui.QImage(data.data, data.width, data.height, QtGui.QImage.Format_RGB888)
		  self.up_camera_signal.emit(image)

		except Exception, e:
		  print(e)

## TODO: Setup Server that will send video information to this appliation 

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = ControlCenter()
	# player = MoviePlayer()
	# player.show()
	sys.exit(app.exec_())