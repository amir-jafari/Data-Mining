import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class inputdialogdemo(QWidget):
    def __init__(self, parent=None):
        super(inputdialogdemo, self).__init__(parent)

        layout = QFormLayout()
        self.btn = QPushButton("Choose from list")
        self.btn.clicked.connect(self.getItem)

        self.le = QLineEdit()
        layout.addRow(self.btn, self.le)
        self.btn1 = QPushButton("get name")
        self.btn1.clicked.connect(self.gettext)

        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)
        self.btn2 = QPushButton("Enter an integer")
        self.btn2.clicked.connect(self.getint)

        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)
        self.setLayout(layout)
        self.setWindowTitle("Input Dialog demo")

    def getItem(self):
        items = ("C", "C++", "Java", "Python")

        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "list of languages", items, 0, False)

        if ok and item:
            self.le.setText(item)

    def gettext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')

        if ok:
            self.le1.setText(str(text))

    def getint(self):
        num, ok = QInputDialog.getDouble(self, "integer input dualog", "enter a number")

        if ok:
            self.le2.setText(str(num))


def main():
    app = QApplication(sys.argv)
    ex = inputdialogdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()