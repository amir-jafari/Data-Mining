from math import sqrt, sin, cos, pi, radians
I_x = 100
I_y = 0
Degree = 10
x, y = eval(input("Enter satellite coordinates (x,y):"))
d1 = sqrt((I_x - x)*(I_x - x) + (I_y - y)*(I_y - y))
x_old = x
x = x*(cos(radians(Degree))) - y*(sin(radians(Degree)))
y = x_old*(sin(radians(Degree))) + y*(cos(radians(Degree)))
d2 = sqrt((I_x - x)*(I_x - x) + (I_y - y)*(I_y - y))
print("Difference in distances: %.3f" % (d2 - d1))
print('#',50*"-")