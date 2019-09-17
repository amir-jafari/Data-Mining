import matplotlib.pyplot as plt
import numpy as np
x16 = np.linspace(-4, 4, 1000)
y16 = .25 * (x16 + 4.) * (x16 + 1) * (x16 - 2)
plt.title('Speed Plot vs. Average')
plt.xlabel('Speed')
plt.ylabel('Average')
plt.plot(x16, y16, c = 'k')
plt.show()
print('#',50*"-")

# -----------------------
x16 = np.linspace(-4, 4, 1000)
y16 = .25 * (x16 + 4.) * (x16 + 1) * (x16 - 2)
box = {
'facecolor' : '.75',
'edgecolor' : 'k',
'boxstyle' : 'round'
}
plt.text(-0.5, -0.20, 'Mark Here', bbox = box)
plt.plot(x16, y16, c = 'k')
plt.show()
print('#',50*"-")
# -----------------------
x16 = np.linspace(-4, 4, 1000)
y16 = .25 * (x16 + 4.) * (x16 + 1) * (x16 - 2)

plt.annotate('Mark Here', ha = 'center', va = 'bottom',
             xytext = (-1.5, 3.), xy = (0.75, -2.7),
             arrowprops = { 'facecolor' : 'black', 'shrink' : 0.05 })

plt.plot(x16, y16, c = 'k')
plt.show()
print('#',50*"-")
# -----------------------
x17 = np.linspace(0, 6, 1024)
y17 = np.sin(x17)
y18 = np.cos(x17)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x17, y17, c = 'k', lw = 3., label = 'sin(X)')
plt.plot(x17, y18, c = '.5', lw = 3., ls = '--', label = 'cos(X)')
plt.legend()
plt.grid(True)
plt.show()
print('#',50*"-")