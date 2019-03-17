__author__ = 'Anthony Torlucci'
__version__ = '0.0.1'

# import python standard modules
import sys

# import 3rd party libraries
from PyQt4 import QtCore, QtGui
import numpy
import pyqtgraph


# import local python

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle('Simple Sinc Function UI')
        self.window = pyqtgraph.GraphicsWindow()
        self.window.setBackground('w')
        self.sinc_plot = self.window.addPlot(title='Sinc Function')
        self.sinc_plot.showGrid(x=True, y=True, alpha=0.5)
        self.setCentralWidget(self.window)
        # add a slider to change the coda of the sinc function
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        # initialize the time axis (this will not change)
        self.t = numpy.linspace(-0.500, 0.500, num=1000, endpoint=True)
        # a will change the coda of the sinc function
        self.a = 1
        #
        # add the menubar with the method createMenuBar()
        self.createMenuBar()
        # add the dock widget with the method createDockWidget()
        self.createDockWidget()
        #
        # first set the default value to a
        self.slider.setValue(self.a)
        # when the slider is changed, it emits a signal and sends an integer value
        # we send that value to a method called slider value changed that updates the value a
        self.slider.valueChanged.connect(self.sliderValueChanged)
        # finally draw the curve

    def createMenuBar(self):
        # file menu actions
        exit_action = QtGui.QAction('&Exit', self)
        exit_action.triggered.connect(self.close)
        # create an instance of menu bar
        menubar = self.menuBar()
        # add file menu and file menu actions
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)

    def createDockWidget(self):
        my_dock_widget = QtGui.QDockWidget()
        my_dock_widget.setObjectName('Control Panel')
        my_dock_widget.setAllowedAreas(QtCore.Qt.TopDockWidgetArea | QtCore.Qt.BottomDockWidgetArea)
        # create a widget to house user control widgets like sliders
        my_house_widget = QtGui.QWidget()
        # every widget should have a layout, right?
        my_house_layout = QtGui.QVBoxLayout()
        # add the slider initialized in __init__() to the layout
        my_house_layout.addWidget(self.slider)
        # apply the 'house' layout to the 'house' widget
        my_house_widget.setLayout(my_house_layout)
        # set the house widget 'inside' the dock widget
        my_dock_widget.setWidget(my_house_widget)
        # now add the dock widget to the main window
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, my_dock_widget)

    def sliderValueChanged(self, int_value):
        self.a = int_value
        self.drawCurve()

    def drawCurve(self):
        self.sinc_plot.clear()
        self.my_sinc = numpy.sin(self.a * numpy.pi * self.t) / (self.a * numpy.pi * self.t)
        self.sinc_plot.plot(self.t, self.my_sinc, pen='b')


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Simple Sinc Function UI')
    window = Window()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()