'''
In the application we will implement controls and triggers
the controls that oversee here are:
   Checkbox
   TextBox
   Radio buttoms
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication
from PyQt5.QtWidgets import QCheckBox    # checkbox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt  # Control status
from PyQt5.QtWidgets import  QWidget,QLabel, QVBoxLayout, QHBoxLayout, QGridLayout

#::------------------------------------------------------------------------------------
#:: Class: Check Control
#::------------------------------------------------------------------------------------
class CheckControlClass(QMainWindow):
    send_fig = pyqtSignal(str)  # To manage the signals PyQT manages the communication

    def __init__(self):
        #::--------------------------------------------------------
        # Initialize the values of the class
        # Here the class inherits all the attributes and methods from the QMainWindow
        #::--------------------------------------------------------
        super(CheckControlClass, self).__init__()

        self.Title = 'Title : Control Title '
        self.initUi()

    def initUi(self):
        #::--------------------------------------------------------------
        #  We create the type of layout QVBoxLayout (Vertical Layout )
        #  This type of layout comes from QWidget
        #::--------------------------------------------------------------
        self.setWindowTitle(self.Title)
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout(self.main_widget)   # Creates vertical layout

        Cbox = QCheckBox('Show title', self)
        Cbox.move(20, 20)
        Cbox.toggle()
        Cbox.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)

        self.layout.addWidget(Cbox)                   # Add Check box to vertical loyout
        self.setCentralWidget(self.main_widget)       # Creates the window with all the elements
        self.resize(300, 100)                         # Resize the window


    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Title : Control Title ')
        else:
            self.setWindowTitle(' ')


#::-------------------------------------------------------------
#:: Definition of a Class for the main manu in the application
#::-------------------------------------------------------------
class Menu(QMainWindow):

    def __init__(self):

        super().__init__()
        #::-----------------------
        #:: variables use to set the size of the window that contains the menu
        #::-----------------------
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 300

        #:: Title for the application

        self.Title = 'Demo PyQt5 - No.4 : Controls and Triggers'

        #:: The initUi is call to create all the necessary elements for the menu

        self.initUI()

    def initUI(self):

        #::-------------------------------------------------
        # Creates the manu and the items
        #::-------------------------------------------------
        self.setWindowTitle(self.Title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar()
        #::-----------------------------
        # 1. Create the menu bar
        # 2. Create an item in the menu bar
        # 3. Creaate an action to be executed the option in the  menu bar is choosen
        #::-----------------------------
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')

        #:: Add another option to the Menu Bar

        exampleWin = mainMenu.addMenu ('Controls')

        #::--------------------------------------
        # Exit action
        # The following code creates the the da Exit Action along
        # with all the characteristics associated with the action
        # The Icon, a shortcut , the status tip that would appear in the window
        # and the action
        #  triggered.connect will indicate what is to be done when the item in
        # the menu is selected
        # These definitions are not available until the button is assigned
        # to the menu
        #::--------------------------------------

        exitButton = QAction(QIcon('enter.png'), '&Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        #:: This line adds the button (item element ) to the menu

        fileMenu.addAction(exitButton)

        #::-----------------------------------------------------------
        #:: Add button to include a Checkbox
        #::-----------------------------------------------------------

        exampleCheckControl = QAction("Checkbox", self)
        exampleCheckControl.setStatusTip("Example of Checkbox")
        exampleCheckControl.triggered.connect(self.ExampleCheckControl)

        #:: We addd the exampleCheckControl to the menu examples
        exampleWin.addAction(exampleCheckControl)

        #:: Creates an empty list of dialogs to keep track of
        #:: all the iterations

        self.dialogs = list()

        #:: This line shows the windows
        self.show()


    def ExampleCheckControl(self):
        dialog = CheckControlClass()
        self.dialogs.append(dialog)  # Appends the list of dialogs
        dialog.show()     # Show the window

#::------------------------
#:: Application starts here
#::------------------------

def main():
    app = QApplication(sys.argv)  # creates the PyQt5 application
    mn = Menu()  # Cretes the menu
    sys.exit(app.exec_())  # Close the application

if __name__ == '__main__':
    main()