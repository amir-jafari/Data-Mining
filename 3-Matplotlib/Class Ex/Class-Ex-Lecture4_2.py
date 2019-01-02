# =================================================================
# Class_Ex1:
# Class_Ex1:
# Find the slope of the following curve for each of its points
#                  y = np.exp(-x ** 2)
# Then plot it with the original curve np.exp(-X ** 2) in the range
# (-3, 3) with 100 points in the range
# ----------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
def plot_slope(x, y):
    xs = x[1:] - x[:-1]
    ys = y[1:] - y[:-1]
    plt.plot(x[1:], ys / xs)
x = np.linspace(-3, 3, 100)
y = np.exp(-x ** 2)
plt.plot(x, y)
plot_slope(x, y)
plt.show()





# =================================================================
# Class_Ex2:

# ----------------------------------------------------------------





# =================================================================
# Class_Ex3: 

# ----------------------------------------------------------------





