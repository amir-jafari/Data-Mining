import numpy
import scipy
import matplotlib.pyplot as plt

import scipy.ndimage
import numpy as np
text = plt.imread('image.png')
letterE = text[37:53,275:291]
corr = scipy.ndimage.correlate(text,letterE)
eLocations = (corr >= 0.95 * corr.max())
CorrLocIndex = np.where(eLocations==True)
x=CorrLocIndex[1]
print(x)
y=CorrLocIndex[0]
print(y)
thefig=plt.figure()
plt.subplot(211)
plt.imshow(text, cmap=plt.cm.gray, interpolation='nearest')
plt.subplot(212)
plt.imshow(text, cmap=plt.cm.gray, interpolation='nearest')
plt.autoscale(False)
plt.plot(x,y,'wo',markersize=10)
plt.axis('off')
plt.show()
print('#',50*"-")