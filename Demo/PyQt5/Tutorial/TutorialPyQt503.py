
#::----------------------------------------------------------------
#:: To create a Menu with options this are the libraries and components that
#:: requiered. For each new option we will be o adding new components
#::----------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox   # No.2

from PyQt5.QtCore import pyqtSlot       # No. 3
from PyQt5.QtCore import pyqtSignal     # No. 3
from PyQt5.QtWidgets import  QWidget,QLabel, QVBoxLayout, QHBoxLayout, QGridLayout # No. 3


#::------------------------------------------------------------------------------------
#:: Class Vertical Layout   # No. 3
#::------------------------------------------------------------------------------------
class VLayoutclass(QMainWindow):  ## All the class was added in No. 3 Section
    send_fig = pyqtSignal(str)  # To manage the signals PyQT manages the communication

    def __init__(self):
        #::--------------------------------------------------------
        # Initialize the values of the class
        # Here the class inherits all the attributes and methods from the QMainWindow
        #::--------------------------------------------------------
        super(VLayoutclass, self).__init__()

        self.Title = 'Vertical Layout'
        self.initUi()

    def initUi(self):
        #::--------------------------------------------------------------
        #  We create the type of layout QVBoxLayout (Vertical Layout )
        #  This type of layout comes from QWidget
        #::--------------------------------------------------------------
        self.setWindowTitle(self.Title)
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout(self.main_widget)   # Creates vertical layout
        self.label1 = QLabel("This is Line 1")        # Creates label1
        self.label2 = QLabel("This is Line 2")        # Creates label2
        self.layout.addWidget(self.label1)            # Add label 1 to  layout
        self.layout.addWidget(self.label2)            # Add label 2 to layout
        self.setCentralWidget(self.main_widget)       # Creates the window with all the elements
        self.resize(300, 100)                         # Resize the window


#::------------------------------------------------------------------------------------
#:: Class Horizontal Layout   # No. 3
#::------------------------------------------------------------------------------------
class HLayoutclass(QMainWindow):  ## All the class was added in No. 3 Section
    send_fig = pyqtSignal(str)  # To manage the signals PyQT manages the communication

    def __init__(self):
        #::--------------------------------------------------------
        # Initialize the values of the class
        # Here the class inherits all the attributes and methods from the QMainWindow
        #::--------------------------------------------------------
        super(HLayoutclass, self).__init__()

        self.Title = 'Horizontal Layout'
        self.initUi()

    def initUi(self):
        #::--------------------------------------------------------------
        #  We create the type of layout QHBoxLayout (Horizontal Layout )
        #  This type of layout comes from QWidget
        #::--------------------------------------------------------------
        self.setWindowTitle(self.Title)
        self.main_widget = QWidget(self)
        self.layout = QHBoxLayout(self.main_widget)   # Creates horizontal layout
        self.label1 = QLabel("This is Column 1")        # Creates label1
        self.label2 = QLabel("This is Column 2")        # Creates label2
        self.layout.addWidget(self.label1)            # Add label 1 to  layout
        self.layout.addWidget(self.label2)            # Add label 2 to layout
        self.setCentralWidget(self.main_widget)       # Creates the window with all the elements
        self.resize(300, 100)                         # Resize the window


#::------------------------------------------------------------------------------------
#:: Class Horizontal Layout   # No. 3
#::------------------------------------------------------------------------------------
class GLayoutclass(QMainWindow):  ## All the class was added in No. 3 Section
    send_fig = pyqtSignal(str)  # To manage the signals PyQT manages the communication

    def __init__(self):
        #::--------------------------------------------------------
        # Initialize the values of the class
        # Here the class inherits all the attributes and methods from the QMainWindow
        #::--------------------------------------------------------
        super(GLayoutclass, self).__init__()

        self.Title = 'Grid Layout'
        self.initUi()

    def initUi(self):
        #::--------------------------------------------------------------
        #  We create the type of layout QGridLayout (Horizontal Layout )
        #  This type of layout comes from QWidget
        #::--------------------------------------------------------------
        self.setWindowTitle(self.Title)
        self.main_widget = QWidget(self)
        self.layout = QGridLayout(self.main_widget)   # Creates horizontal layout
        self.label1 = QLabel("This is line 1 col 1")        # Creates label1
        self.label2 = QLabel("This is line 1 col 2")        # Creates label2
        self.label3 = QLabel("This is line 2 col 1")        # Creates label3
        self.label4 = QLabel("This is line 2 col 2")        # Creates label4
        self.layout.addWidget(self.label1,0,0)            # Add label 1 to  layout
        self.layout.addWidget(self.label2,0,1)            # Add label 2 to layout
        self.layout.addWidget(self.label3,1,0)            # Add label 3 to layout
        self.layout.addWidget(self.label4,1,1)            # Add label 4 to layout

        self.setCentralWidget(self.main_widget)       # Creates the window with all the elements
        self.resize(300, 100)                         # Resize the window


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

        self.Title = 'Demo PyQt5 - No.1 : Menus'

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

        exampleWin = mainMenu.addMenu ('Examples')   # No. 2

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

        #::----------------------------------------------------
        #::Add Example 1 We create the item Menu Example1
        #::This option will present a message box upon request
        #::----------------------------------------------------

        example1Button = QAction("Example1", self)    # No. 2
        example1Button.setStatusTip("Print Hello World 1")   # No. 2
        example1Button.triggered.connect(self.printhello)    # No. 2

        #:: We addd the example1Button action to the Menu Examples
        exampleWin.addAction(example1Button)    # No. 2

        #::-----------------------------------------------------------
        #:: Add button for Vertical Layout   # No.3
        #::-----------------------------------------------------------

        example2Button = QAction("Vertical", self)    # No. 3
        example2Button.setStatusTip("Example of vertical layout")  # No. 3
        example2Button.triggered.connect(self.VLayout)  # No. 3

        #:: We addd the example2Button to the menu examples
        exampleWin.addAction(example2Button)    # No. 3

        #::-----------------------------------------------------------
        #:: Add button for Horizontal Layout   # No.3
        #::-----------------------------------------------------------

        example3Button = QAction("Horizontal", self)  # No. 3
        example3Button.setStatusTip("Example of horizontal layout")  # No. 3
        example3Button.triggered.connect(self.HLayout)  # No. 3

        #:: We addd the example2Button to the menu examples
        exampleWin.addAction(example3Button)  # No. 3

        #::-----------------------------------------------------------
        #:: Add button for Grid Layout   # No.3
        #::-----------------------------------------------------------

        example4Button = QAction("Grid", self)  # No. 3
        example4Button.setStatusTip("Example of Grid layout")  # No. 3
        example4Button.triggered.connect(self.GLayout)  # No. 3

        #:: We addd the example2Button to the menu examples
        exampleWin.addAction(example4Button)  # No. 3


        #:: Creates an empty list of dialogs to keep track of
        #:: all the iterations

        self.dialogs = list()

        #:: This line shows the windows
        self.show()

    def printhello(self):    # No. 2
        QMessageBox.about(self, "Results Example1", "Hello World!!!")  # No. 2

    def VLayout(self):  # No. 3
        dialog = VLayoutclass()  #  Creates an object with Vertical class
        self.dialogs.append(dialog)  # Appends the list of dialogs
        dialog.show()     # Show the window

    def HLayout(self):  # No. 3
        dialog = HLayoutclass()    # Creates an object with the Horizontal class
        self.dialogs.append(dialog) # Appeds the list of dialogs
        dialog.show()   # Show the window

    def GLayout(self):  # No. 3
        dialog = GLayoutclass()    # Creates an object with the Horizontal class
        self.dialogs.append(dialog) # Appeds the list of dialogs
        dialog.show()   # Show the window

#::------------------------
#:: Application starts here
#::------------------------

def main():
    app = QApplication(sys.argv)  # creates the PyQt5 application
    mn = Menu()  # Cretes the menu
    sys.exit(app.exec_())  # Close the application

if __name__ == '__main__':
    main()