from PyQt4 import QtGui, QtCore


class RenderManagement(QtGui.QWidget):
    def __init__(self):
        super(RenderManagement, self).__init__()

        self.v_layout = QtGui.QVBoxLayout(self)

        # Create 5 dynamic items
        for i in range(5):
            item = LightItem()
            item.setTitle("LightItem%d" % i)
            self.v_layout.addWidget(item)

            # watch for the moveRequested signal on each item
            item.moveRequested.connect(self.moveLightItem)

    def moveLightItem(self, direction):

        # the sender should always be a LightItem instance
        obj = self.sender()
        print( "Move LightItem %s in direction %s" % (obj, direction))

        # what is the current index of the widget in the layout?
        idx = self.v_layout.indexOf(obj)
        if idx == -1:
            print("Widget is not in the layout:", obj)
            return

        if direction == QtCore.Qt.Key_Up:
            # next index down
            idx = max(idx - 1, 0)

        elif direction == QtCore.Qt.Key_Down:
            # next index up
            idx = min(idx + 1, self.v_layout.count() - 1)

        else:
            print("Not a key up or down")
            return

        # will insert the widget into a differnt index of the layout
        self.v_layout.insertWidget(idx, obj)


class LightItem(QtGui.QGroupBox):
    # custom signal, emitting the Qt.Key_X
    moveRequested = QtCore.pyqtSignal(int)

    def __init__(self):
        super(LightItem, self).__init__()

        # Generic layout of widgets
        self.v_layout = QtGui.QVBoxLayout(self)
        self.v_layout.setMargin(2)

        self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

        self.left = QtGui.QGroupBox('Left')

        self.lineEdit = QtGui.QLineEdit()
        self.left_layout = QtGui.QVBoxLayout(self.left)
        self.left_layout.addWidget(self.lineEdit)

        self.right = QtGui.QGroupBox('Right')

        self.splitter.addWidget(self.left)
        self.splitter.addWidget(self.right)

        self.v_layout.addWidget(self.splitter)

        # have LightItem watch all events on the QLineEdit,
        # so that we do not have to subclass QLineEdit
        self.lineEdit.installEventFilter(self)

    def eventFilter(self, obj, event):
        # Only watch for specific Key presses on the QLineEdit
        # Everything else is pass-thru
        if obj is self.lineEdit and event.type() == event.KeyPress:
            key = event.key()
            if key in (QtCore.Qt.Key_Up, QtCore.Qt.Key_Down):
                print("Emitting moveRequested() for obj", obj)
                self.moveRequested.emit(event.key())
                return True

        return False


if __name__ == "__main__":
    app = QtGui.QApplication([])

    manager = RenderManagement()
    manager.resize(800, 600)
    manager.show()

    app.exec_()