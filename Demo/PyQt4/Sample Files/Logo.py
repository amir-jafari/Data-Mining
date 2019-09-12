import sys
from PyQt4 import QtGui, QtSvg

app = QtGui.QApplication(sys.argv)
svgWidget = QtSvg.QSvgWidget('pic1.svg')
svgWidget.setGeometry(50,50,759,668)
svgWidget.show()

sys.exit(app.exec_())