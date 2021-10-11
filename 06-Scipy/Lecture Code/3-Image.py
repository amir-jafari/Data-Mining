import numpy
import scipy
import matplotlib.pyplot as plt


import scipy.misc
img=scipy.misc.ascent()
plt.imshow(img)
plt.show()
print(img[0:3,0:7])
print(img)
img=scipy.misc.face()
plt.imshow(img)
plt.show()
print(img[0:3,0:7])
print(img)
print('#',50*"-")