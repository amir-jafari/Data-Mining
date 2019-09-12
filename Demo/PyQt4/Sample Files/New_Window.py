import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class OtherWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        layout = QHBoxLayout()
        lineEdit = QLineEdit()
        lineEdit.setText("Just to fill up the dialog")
        layout.addWidget(lineEdit)

        self.widget = QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        self.setWindowTitle("Win2")


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        layout = QHBoxLayout()
        button = QPushButton()
        layout.addWidget(button)

        self.widget = QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        self.setWindowTitle("Win1")

        self.connect(button, SIGNAL('clicked()'), self.newWindow)

    def newWindow(self):
        self.myOtherWindow = OtherWindow()
        self.myOtherWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setGeometry(100, 100, 200, 200)
    mainWindow.show()
    sys.exit(app.exec_())