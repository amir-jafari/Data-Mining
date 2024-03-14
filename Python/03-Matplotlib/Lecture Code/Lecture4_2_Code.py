import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(10)
y1 = np.sin(x1)
plt.plot(x1, y1)
plt.draw()
plt.show()
print('#',50*"-")
# -----------------------
x2 = np.linspace(0, 2 * np.pi, 100)
y2 = np.sin(x2)
plt.plot(x2, y2)
plt.show()
x3 = np.linspace(1, 3, 100)
y3 = x3 ** 2 - 2 * x3 + 1
plt.plot(x3, y3)
plt.show()
print('#',50*"-")
# -----------------------
x4 = np.linspace(0, 2 * np.pi, 100)
ya = np.sin(x4)
yb = np.cos(x4)
plt.plot(x4, ya)
plt.plot(x4, yb)
plt.show()
print('#',50*"-")
# -----------------------
x5 = np.linspace(-3, 3, 100)
y5 = np.exp(-x5 ** 2)
plt.plot(x5, y5)
plt.show()
print('#',50*"-")
# -----------------------
x6 = []
y6 = []
for line in open('data1.txt', 'r'):
    data = [float(s) for s in line.split()]
    x6.append(data[0])
    y6.append(data[1])
plt.plot(x6, y6)
plt.show()

with open('data1.txt', 'r') as f:
    x7, y7 = zip(*[[float(s) for s in line.split()] for line in f])
plt.plot(x7, y7)
plt.show()

data = np.loadtxt('data1.txt')
plt.plot(data[:,0], data[:,1])
plt.show()
print('#',50*"-")
# -----------------------
data = np.random.rand(1024, 2)
plt.scatter(data[:,0], data[:,1])
plt.show()
print('#',50*"-")
# -----------------------
data = [5, 10, 30, 8]
plt.bar(range(len(data)), data)
plt.show()
print('#',50*"-")
# -----------------------
plt.bar(range(len(data)), data, width = 1.)
plt.show()

plt.barh(range(len(data)), data)
plt.show()
print('#',50*"-")
# -----------------------
data = np.random.rand(3,4)
x8 = np.arange(4)
plt.bar(x8 + 0.00, data[0], color = 'b', width = 0.25)
plt.bar(x8 + 0.25, data[1], color = 'g', width = 0.25)
plt.bar(x8 + 0.50, data[2], color = 'r', width = 0.25)
plt.show()
print('#',50*"-")
# -----------------------
a = np.random.rand(4)
b = np.random.rand(4)
x9 = np.arange(4)
plt.bar(x9, a, color = 'b')
plt.bar(x9, b, color = 'r', bottom = a)
plt.show()
print('#',50*"-")
# -----------------------
a = np.random.rand(4)
b = np.random.rand(4)
c = np.random.rand(4)
x10 = np.arange(4)
plt.bar(x10, a, color = 'b' )
plt.bar(x10, b, color = 'g', bottom = a)
plt.bar(x10, c, color = 'r', bottom = a + b)
plt.show()
print('#',50*"-")
# -----------------------
BMI = np.array([5., 30., 45., 22.])
age = np.array( [5., 25., 50., 20.])
x11 = np.arange(4)
plt.barh(x11, BMI, color = 'r')
plt.barh(x11, -age, color = 'b')
plt.show()
print('#',50*"-")
# -----------------------
data = np.array([5, 25, 50, 20])
plt.pie(data)
plt.show()

x12 = np.random.randn(1000)
plt.hist(x12, bins = 20)
plt.show()
print('#',50*"-")
# -----------------------
data = np.random.randn(100)
plt.boxplot(data)
plt.show()

data = np.random.randn(100, 5)
plt.boxplot(data)
plt.show()
print('#',50*"-")
# -----------------------
import matplotlib.tri as tri
data = np.random.rand(100, 2)
triangles = tri.Triangulation(data[:,0], data[:,1])
plt.triplot(triangles)
plt.show()
print('#',50*"-")
# -----------------------
def pdf(X, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (X - mu) ** 2)
x13 = np.linspace(-6, 6, 1000)
for i in range(5):
    samples = np.random.standard_normal(50)
    mu, sigma = np.mean(samples), np.std(samples)
    plt.plot(x13, pdf(x13, mu, sigma), color = '.75')
    plt.plot(x13, pdf(x13, 0., 1.), color = 'k')
plt.show()
print('#',50*"-")
# -----------------------
a = np.random.standard_normal((100, 2))
a += np.array((-2, -2)) # Center
b = np.random.standard_normal((100, 2))
b += np.array((2, 2)) # Center
plt.scatter(a[:,0], a[:,1], color = '.2')
plt.scatter(b[:,0], b[:,1], color = '.8')
plt.show()
print('#',50*"-")
# -----------------------
data = np.random.standard_normal((100, 2))
plt.scatter(data[:,0], data[:,1], color = '1.0', edgecolor='0.0')
plt.show()
print('#',50*"-")
# -----------------------
values = np.random.random_integers(99, size = 50)
color_set = ('.00', '.25', '.50', '.75')
color_list = [color_set[(len(color_set) * val) // 100] for val in
values]
plt.bar(np.arange(len(values)), values, color = color_list)
plt.show()
print('#',50*"-")
# -----------------------
import matplotlib.cm as cm
N = 256
angle = np.linspace(0, 8 * 2 * np.pi, N)
radius = np.linspace(.5, 1., N)
X = radius * np.cos(angle)
Y = radius * np.sin(angle)
plt.scatter(X, Y, c = angle, cmap = cm.hsv)
plt.show()
print('#',50*"-")
# -----------------------
import matplotlib.colors as col
values = np.random.random_integers(99, size = 50)
cmap = cm.ScalarMappable(col.Normalize(0, 99), cm.binary)
plt.bar(np.arange(len(values)), values, color = cmap.to_rgba(values))
plt.show()
print('#',50*"-")
# -----------------------
x13 = np.linspace(-6, 6, 1024)
plt.plot(x13, pdf(x13, 0., 1.), color = 'k', linestyle = 'solid')
plt.plot(x13, pdf(x13, 0., .5), color = 'k', linestyle = 'dashed')
plt.plot(x13, pdf(x13, 0., .25), color = 'k', linestyle = 'dashdot')
plt.show()

for i in range(64):
    samples = np.random.standard_normal(50)
    mu, sigma = np.mean(samples), np.std(samples)
    plt.plot(x13, pdf(x13, mu, sigma), color = '.75', linewidth = .5)
plt.plot(x13, pdf(x13, 0., 1.), color = 'y', linewidth = 3.)
plt.show()
print('#',50*"-")
# -----------------------
a = np.random.standard_normal((100, 2))
a += np.array((-2, -2)) # Center
b = np.random.standard_normal((100, 2))
b += np.array((2, 2)) # Center
plt.scatter(a[:,0], a[:,1], color = 'k', marker = 'x')
plt.scatter(b[:,0], b[:,1], color = 'k', marker = '^')
plt.show()
print('#',50*"-")
# -----------------------
X = np.linspace(-6, 6, 1024)
Y1 = np.sinc(X)
Y2 = np.sinc(X) + 1
plt.plot(X, Y1, marker = 'o', color = '.75')
plt.plot(X, Y2, marker = 'o', color = 'k', markevery = 32)
plt.show()

a = np.random.standard_normal((100, 2))
a += np.array((-1, -1))
b = np.random.standard_normal((100, 2))
b += np.array((1, 1))
plt.scatter(b[:,0], b[:,1], c = 'r', s = 100)
plt.scatter(a[:,0], a[:,1], c = 'b', s = 25)
plt.show()
print('#',50*"-")
# -----------------------
import matplotlib.path as mpath
shape_description = [
( 1., 2., mpath.Path.MOVETO),
( 1., 1., mpath.Path.LINETO),
( 2., 1., mpath.Path.LINETO),
( 2., -1., mpath.Path.LINETO),
( 1., -1., mpath.Path.LINETO),
( 1., -2., mpath.Path.LINETO),
(-1., -2., mpath.Path.LINETO),
(-1., -1., mpath.Path.LINETO),
(-2., -1., mpath.Path.LINETO),
(-2., 1., mpath.Path.LINETO),
(-1., 1., mpath.Path.LINETO),
(-1., 2., mpath.Path.LINETO),
( 0., 0., mpath.Path.CLOSEPOLY),
]
u, v, codes = zip(*shape_description)
my_marker = mpath.Path(np.asarray((u, v)).T, codes)
data = np.random.rand(10, 10)
plt.scatter(data[:,0], data[:, 1], c = 'b', marker = my_marker, s = 120)
plt.show()
print('#',50*"-")
# -----------------------
x15 = np.linspace(-6, 6, 1024)
y15 = np.sinc(x15)

plt.plot(x15, y15,
linewidth = 3., color = 'k',
markersize = 9, markeredgewidth = 1.5,
markerfacecolor = '.75', markeredgecolor = 'k',
marker = 'o', markevery = 32)
plt.show()
print('#',50*"-")
# -----------------------
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
x16 = np.linspace(-4, 4, 1000)
y16 = .25 * (x16 + 4) * (x16 + 1) * (x16 - 2)
plt.title('A polynomial' r'$f(x)=\frac{1}{4}(x+4)(x+1)(x-2)$')
plt.plot(x16, y16, c = 'k')
plt.show()
print('#',50*"-")
# -----------------------
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
# -----------------------
import matplotlib.patches as patches
# Circle
shape = patches.Circle((0, 0), radius = 1., color = '.75')
plt.gca().add_patch(shape)
# Rectangle
shape = patches.Rectangle((2.5, -.5), 2., 1., color = '.75')
plt.gca().add_patch(shape)
# Ellipse
shape = patches.Ellipse((0, -2.), 2., 1., angle = 45., color =
'.75')
plt.gca().add_patch(shape)
# Fancy box
shape = patches.FancyBboxPatch((2.5, -2.5), 2., 1., boxstyle =
'sawtooth', color = '.75')
plt.gca().add_patch(shape)
# Display all
plt.grid(True)
plt.axis('scaled')
plt.show()
print('#',50*"-")
# -----------------------
import matplotlib.ticker as ticker
X = np.linspace(-15, 15, 1000)
Y = np.sinc(X)
ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.grid(True, which='both')
plt.plot(X, Y)
plt.show()
print('#',50*"-")
# -----------------------