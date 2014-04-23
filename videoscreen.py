import PySide
import sys

from PySide import QtCore, QtGui
from PySide.QtCore import QX11EmbedWindow
from PySide.QtGui import QX11EmbedContainer 

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


if __name__ == '__main__':

	import sys

	app = QGui.QApplication(sys.argv)
	player = MoviePlayer()
	player.show()
	sys.exit(app.exec_())