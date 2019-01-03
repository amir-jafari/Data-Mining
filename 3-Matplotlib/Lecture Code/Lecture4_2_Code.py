import matplotlib.pyplot as plt
import numpy as np
# x1 = np.arange(10)
# y1 = np.sin(x1)
# plt.plot(x1, y1)
# plt.draw()
# plt.show()
# print('#',50*"-")
# # -----------------------
# x2 = np.linspace(0, 2 * np.pi, 100)
# y2 = np.sin(x2)
# plt.plot(x2, y2)
# plt.show()
# x3 = np.linspace(1, 3, 100)
# y3 = x3 ** 2 - 2 * x3 + 1
# plt.plot(x3, y3)
# plt.show()
# print('#',50*"-")
# # -----------------------
# x4 = np.linspace(0, 2 * np.pi, 100)
# ya = np.sin(x4)
# yb = np.cos(x4)
# plt.plot(x4, ya)
# plt.plot(x4, yb)
# plt.show()
# print('#',50*"-")
# # -----------------------
# x5 = np.linspace(-3, 3, 100)
# y5 = np.exp(-x5 ** 2)
# plt.plot(x5, y5)
# plt.show()
# print('#',50*"-")
# -----------------------
# x6 = []
# y6 = []
# for line in open('data1.txt', 'r'):
#     data = [float(s) for s in line.split()]
#     x6.append(data[0])
#     y6.append(data[1])
# plt.plot(x6, y6)
# plt.show()
#
# with open('data1.txt', 'r') as f:
#     x7, y7 = zip(*[[float(s) for s in line.split()] for line in f])
# plt.plot(x7, y7)
# plt.show()
#
# data = np.loadtxt('data1.txt')
# plt.plot(data[:,0], data[:,1])
# plt.show()
# print('#',50*"-")
# # -----------------------
# data = np.random.rand(1024, 2)
# plt.scatter(data[:,0], data[:,1])
# plt.show()
# print('#',50*"-")
# # -----------------------
# data = [5, 10, 30, 8]
# plt.bar(range(len(data)), data)
# plt.show()
# print('#',50*"-")
# # -----------------------
# plt.bar(range(len(data)), data, width = 1.)
# plt.show()
#
# plt.barh(range(len(data)), data)
# plt.show()
# print('#',50*"-")
# # -----------------------
# data = np.random.rand(3,4)
# x8 = np.arange(4)
# plt.bar(x8 + 0.00, data[0], color = 'b', width = 0.25)
# plt.bar(x8 + 0.25, data[1], color = 'g', width = 0.25)
# plt.bar(x8 + 0.50, data[2], color = 'r', width = 0.25)
# plt.show()
# print('#',50*"-")
# # -----------------------
# a = np.random.rand(4)
# b = np.random.rand(4)
# x9 = np.arange(4)
# plt.bar(x9, a, color = 'b')
# plt.bar(x9, b, color = 'r', bottom = a)
# plt.show()
# print('#',50*"-")
# # -----------------------
# a = np.random.rand(4)
# b = np.random.rand(4)
# c = np.random.rand(4)
# x10 = np.arange(4)
# plt.bar(x10, a, color = 'b' )
# plt.bar(x10, b, color = 'g', bottom = a)
# plt.bar(x10, c, color = 'r', bottom = a + b)
# plt.show()
# print('#',50*"-")
# # -----------------------
# BMI = np.array([5., 30., 45., 22.])
# age = np.array( [5., 25., 50., 20.])
# x11 = np.arange(4)
# plt.barh(x11, BMI, color = 'r')
# plt.barh(x11, -age, color = 'b')
# plt.show()
# print('#',50*"-")
# # -----------------------
# data = np.array([5, 25, 50, 20])
# plt.pie(data)
# plt.show()
#
# x12 = np.random.randn(1000)
# plt.hist(x12, bins = 20)
# plt.show()
# print('#',50*"-")
# # -----------------------
# data = np.random.randn(100)
# plt.boxplot(data)
# plt.show()
#
# data = np.random.randn(100, 5)
# plt.boxplot(data)
# plt.show()
# print('#',50*"-")
# # -----------------------
import matplotlib.tri as tri
data = np.random.rand(100, 2)
triangles = tri.Triangulation(data[:,0], data[:,1])
plt.triplot(triangles)
plt.show()