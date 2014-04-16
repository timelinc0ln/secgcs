import PySide.QtCore
import PySide.QtGui
import sys
import time

import SensorWidgets


def run_app():
    app = PySide.QtGui.QApplication(sys.argv)
    frame = SensorWidgets.SensorWindow()
    # Create a timer for the event loop.
    timer = PySide.QtCore.QTimer()
    timer.start(1000)
    # Run the application.
    frame.run(app)


if __name__ in ['__main__']:
    run_app()

