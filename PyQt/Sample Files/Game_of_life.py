import sys
import numpy as np
from PyQt4 import QtGui

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from functools import partial

class Game_of_life(QtGui.QWidget):
    def __init__(self, N, ON, OFF):
        super(Game_of_life, self).__init__()
        self.N = N
        self.ON = ON
        self.OFF = OFF
        self.vals = [ON, OFF]
        self.grid = np.random.choice(self.vals, N*N, p=[0.2, 0.8]).reshape(N, N)
        self.start()

    def start(self):
        self.setWindowTitle('Game of life')
        gridLayout = QtGui.QGridLayout()
        self.setLayout(gridLayout)

        #Figure and subplot
        figure = plt.figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)
        canvas.draw()

        self.mat = ax.matshow(self.grid)
        ani = animation.FuncAnimation(figure, self.update, interval=50, save_count=50)

        #button
        restart = QtGui.QPushButton("Restart game of life")
        restart.clicked.connect(partial(self.restart_animation, ax=ax, figure=figure))

        gridLayout.addWidget(canvas,0,0)
        gridLayout.addWidget(restart, 1,0)

        self.show()
    def update(self, data):
        newGrid = self.grid.copy()
        for i in range(self.N):
            for j in range(self.N):
                total = (self.grid[i, (j-1)%self.N] + self.grid[i, (j+1)%self.N] +
                        self.grid[(i-1)%self.N, j] + self.grid[(i+1)%self.N, j] +
                        self.grid[(i-1)%self.N, (j-1)%self.N] + self.grid[(i-1)%self.N, (j+1)%self.N] +
                        self.grid[(i+1)%self.N, (j-1)%self.N] + self.grid[(i+1)%self.N, (j+1)%self.N])/255
                if self.grid[i, j]  == self.ON:
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = self.OFF
                else:
                    if total == 3:
                        newGrid[i, j] = self.ON
        self.mat.set_data(newGrid)
        self.grid = newGrid

    #simply restarts game data
    def restart_animation(self, ax, figure):
        self.grid = np.random.choice(self.vals, self.N*self.N, p=[0.2, 0.8]).reshape(self.N, self.N)
        self.mat = ax.matshow(self.grid)


def main():
    app = QtGui.QApplication(sys.argv)
    widget = Game_of_life(100, 255, 0)
    #widget can be implement in other layout
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()