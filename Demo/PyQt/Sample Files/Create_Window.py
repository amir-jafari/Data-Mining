import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL
class Main1(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QMainWindow.__init__(self, parent)
    self.button = QtGui.QPushButton('Create other window', self)
    self.other_window = None
    self.connect(self.button, SIGNAL('clicked()'), self.spawnMain2)
    self.connect(self, SIGNAL('main2closed()'), self.clearMain2)
  def spawnMain2(self):
    self.other_window = Main2()
    self.connect(self.other_window, SIGNAL('closed()'), self.main2Closed)
    self.other_window.show()
  def main2Closed(self):
    self.emit(SIGNAL('main2closed()'))
  def clearMain2(self):
    del self.other_window
    self.other_window = None
class Main2(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QMainWindow.__init__(self, parent)
    self.button = QtGui.QPushButton('Quit', self)
    self.connect(self.button, SIGNAL('clicked()'), self.close)
if __name__ == '__main__':
  app = QtGui.QApplication(sys.argv)
  win = Main1()
  win.show()
  sys.exit(app.exec_())