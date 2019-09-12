'''
In the application we will implement controls and triggers
the controls that oversee here are:
    Implementing a Group Box
    Implementing a Graph
    Implementing a Graph with parameters
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtWidgets import QCheckBox    # checkbox
from PyQt5.QtWidgets import QPushButton  # pushbutton
from PyQt5.QtWidgets import QLineEdit    # Lineedit
from PyQt5.QtWidgets import QRadioButton # Radio Buttons
from PyQt5.QtWidgets import QGroupBox    # Group Box


# These components are essential for creating the graphics in pqt5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure     # Figure
#---------------------------------------------------------------------

from numpy.polynomial.polynomial import polyfit
import numpy as np

#----------------------------------------------------------------------
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt  # Control status
from PyQt5.QtWidgets import  QWidget,QLabel, QVBoxLayout, QHBoxLayout, QGridLayout

#::------------------------------------------------------------------------------------
#:: Class: Group Box
#::------------------------------------------------------------------------------------
class GroupBoxClass(QMainWindow):
    send_fig = pyqtSignal(str)  # To manage the signals PyQT manages the communication

    def __init__(self):
        #::--------------------------------------------------------
        # Initialize the values of the class
        # Here the class inherits all the attributes and methods from the QMainWindow
        #::--------------------------------------------------------
        super(GroupBoxClass, self).__init__()

        self.Title = 'Title : Group Box '
        self.initUi()

    def initUi(self):
        #::--------------------------------------------------------------
        #  We create the type of layout QVBoxLayout (Vertical Layout )
        #  This type of layout comes from QWidget
        #::--------------------------------------------------------------
        self.setWindowTitle(self.Title)
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout(self.main_widget)   # Creates vertical layout

        self.groupBox1 = QGroupBox('Features')
        self.groupBox1Layout= QGridLayout()
        self.groupBox1.setLayout(self.groupBox1Layout)


        self.Cbox1 = QCheckBox('Feature 1', self)
        self.Cbox1.setChecked(True)
        self.Cbox2 = QCheckBox('Feature 2', self)
        self.Cbox2.setChecked(True)
        self.groupBox1Layout.addWidget(self.Cbox1, 0, 0)
        self.groupBox1Layout.addWidget(self.Cbox2, 0, 1)

        self.setGeometry(300, 300, 250, 150)

        self.layout.addWidget(self.groupBox1)

        self.setCentralWidget(self.main_widget)       # Creates the window with all the elements
        self.resize(300, 100)                         # Resize the window

#::------------------------------------------------------------------------------------
#:: Class: Line Edit Control
#::------------------------------------------------------------------------------------
class GraphicClass(QMainWindow):
    send_fig = pyqtSignal(str)  # To manage the signals PyQT manages the communication

    def __init__(self):
        #::--------------------------------------------------------
        # Initialize the values of the class
        # Here the class inherits all the attributes and methods from the QMainWindow
        #::--------------------------------------------------------
        super(GraphicClass, self).__init__()

        self.Title = 'Title : Simple Graph '
        self.initUi()

    def initUi(self):
        #::--------------------------------------------------------------
        #  We create the type of layout QVBoxLayout (Vertical Layout )
        #  This type of layout comes from QWidget
        #::--------------------------------------------------------------
        self.setWindowTitle(self.Title)
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout(self.main_widget)   # Creates vertical layout

        #::----------------------------------------------------------------
        #  Creates the containers for the graphic
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)

        self.canvas.setSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Expanding)

        self.canvas.updateGeometry()

        X_1 = [1,2,3,4,5,6,7,8,9,10]
        y_1 = [8,35,40,1,34,33,2,33,11,14]

        self.ax1.scatter(X_1,y_1)

        vtitle = "Example of graph"
        self.ax1.set_title(vtitle)
        self.ax1.set_xlabel("Label for X")
        self.ax1.set_ylabel("Label for y")
        self.ax1.grid(True)

        self.fig.tight_layout()
        self.fig.canvas.draw_idle()


        self.layout.addWidget(self.canvas)

        self.setGeometry(300, 300, 250, 150)

        self.setCentralWidget(self.main_widget)       # Creates the window with all the elements
        self.resize(500, 450)                         # Resize the window
        self.show()

#::------------------------------------------------------------------------------------
#:: Class: Graphic with Params
#::------------------------------------------------------------------------------------
class GraphWParamsClass(QMainWindow):
    send_fig = pyqtSignal(str)  # To manage the signals PyQT manages the communication

    def __init__(self):
        #::--------------------------------------------------------
        # Initialize the values of the class
        # Here the class inherits all the attributes and methods from the QMainWindow
        #::--------------------------------------------------------
        super(GraphWParamsClass, self).__init__()

        self.Title = 'Title : Graphic with Parameters '
        self.initUi()

    def initUi(self):
        #::--------------------------------------------------------------
        #  We create the type of layout QVBoxLayout (Vertical Layout )
        #  This type of layout comes from QWidget
        #::--------------------------------------------------------------
        self.vcolor = "Orange"
        self.setWindowTitle(self.Title)
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout(self.main_widget)   # Creates vertical layout

        # Fist the group boxes are created
        self.groupBox1 = QGroupBox('')
        self.groupBox1Layout= QVBoxLayout()
        self.groupBox1.setLayout(self.groupBox1Layout)

        self.groupBox2 = QGroupBox('Color or Regression Line')
        self.groupBox2Layout = QHBoxLayout()
        self.groupBox2.setLayout(self.groupBox2Layout)

        self.groupBox3 = QGroupBox('Graphic')
        self.groupBox3Layout = QVBoxLayout()
        self.groupBox3.setLayout(self.groupBox3Layout)

        # the checkline is created to be added to the first group
        self.chkline = QCheckBox("Include Regression LIne", self)
        self.chkline.setChecked(True)
        self.chkline.stateChanged.connect(self.onClicked)

        self.groupBox1Layout.addWidget(self.chkline)

        # Radio buttons are create to be added to the second group

        self.b1 = QRadioButton("Orange")
        self.b1.setChecked(True)
        self.b1.toggled.connect(self.onClicked)

        self.b2 = QRadioButton("Blue")
        self.b2.toggled.connect(self.onClicked)

        self.b3 = QRadioButton("Red")
        self.b3.toggled.connect(self.onClicked)

        self.buttonlabel = QLabel(self.vcolor+' is selected')

        self.groupBox2Layout.addWidget(self.b1)
        self.groupBox2Layout.addWidget(self.b2)
        self.groupBox2Layout.addWidget(self.b3)
        self.groupBox2Layout.addWidget(self.buttonlabel)

        # Information to be displayed in the graph
        self.X_1 = np.array( [1,2,3,4,5,6,7,8,9,10])
        self.y_1 = np.array([15,25,30,20,50,55,60,55,70,75])

        # Parameters for the regression line
        self.b, self.m = polyfit(self.X_1, self.y_1, 1)

        # figure and canvas figure to draw the graph is created to

        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)

        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.canvas.updateGeometry()

        # Canvas is added to the third group box
        self.groupBox3Layout.addWidget(self.canvas)


        # Adding to the main layout the groupboxes

        self.layout.addWidget(self.groupBox1)
        self.layout.addWidget(self.groupBox2)
        self.layout.addWidget(self.groupBox3)

        self.setCentralWidget(self.main_widget)       # Creates the window with all the elements
        self.resize(600, 500)                         # Resize the window
        self.onClicked()


    def onClicked(self):

        # Figure is cleared to create the new graph with the choosen parameters
        self.ax1.clear()

        # the buttons are inspect to indicate which one is checked.
        # vcolor is assigned the chosen color
        if self.b1.isChecked():
            self.vcolor = self.b1.text()
        if self.b2.isChecked():
            self.vcolor = self.b2.text()
        if self.b3.isChecked():
            self.vcolor = self.b3.text()

        # the label that displays the selected option
        self.buttonlabel.setText(self.vcolor+' is selected')

        # create the scatter plot , a radio button option could be created
        # to choose a scatter plot or other type of graphic

        self.ax1.scatter(self.X_1, self.y_1)

        # if checkbox for showing regression line is checked
        if self.chkline.isChecked():
            self.ax1.plot(self.X_1, self.b + self.m * self.X_1, '-', color=self.vcolor)

        vtitle = "Example of graph with parameters"
        self.ax1.set_title(vtitle)
        self.ax1.set_xlabel("Label for X")
        self.ax1.set_ylabel("Label for y")
        self.ax1.grid(True)

        # show the plot
        self.fig.tight_layout()
        self.fig.canvas.draw_idle()


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

        self.Title = 'Demo PyQt5 - No.7 : Groups and Graphics'

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

        exampleWin = mainMenu.addMenu ('Graphics')

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
        #:: Add code to include a Checkbox
        #::-----------------------------------------------------------

        exampleGroupBox = QAction("Group Box", self)
        exampleGroupBox.setStatusTip("Example of Group Box")
        exampleGroupBox.triggered.connect(self.ExampleGroupBox)

        #:: We add the exampleCheckControl to the menu examples
        exampleWin.addAction(exampleGroupBox)

        #::------------------------------------------------------------
        #:: Add code to include Text Line and button to implement an action upon request
        #::------------------------------------------------------------

        exampleGraphic =  QAction("Graphic", self)
        exampleGraphic.setStatusTip('Example of Graphic')
        exampleGraphic.triggered.connect(self.ExampleGraphic)

        exampleWin.addAction(exampleGraphic)

        #::------------------------------------------------------------
        #:: Add code to include radio buttons  to implement an action upon request
        #::------------------------------------------------------------

        exampleGWParams =  QAction("Graphic with Parameters ", self)
        exampleGWParams.setStatusTip('Example of Graphic with parameters')
        exampleGWParams.triggered.connect(self.ExampleGraphWParams)

        exampleWin.addAction(exampleGWParams)

        #:: Creates an empty list of dialogs to keep track of
        #:: all the iterations

        self.dialogs = list()

        #:: This line shows the windows
        self.show()


    def ExampleGroupBox(self):
        dialog = GroupBoxClass()
        self.dialogs.append(dialog)  # Appends to the list of dialogs
        dialog.show()     # Show the window

    def ExampleGraphic(self):
        dialog = GraphicClass()
        self.dialogs.append(dialog) # Apppends to the list of dialogs
        dialog.show()

    def ExampleGraphWParams(self):
        dialog = GraphWParamsClass()
        self.dialogs.append(dialog) # Apppends to the list of dialogs
        dialog.show()

#::------------------------
#:: Application starts here
#::------------------------

def main():
    app = QApplication(sys.argv)  # creates the PyQt5 application
    mn = Menu()  # Cretes the menu
    sys.exit(app.exec_())  # Close the application

if __name__ == '__main__':
    main()