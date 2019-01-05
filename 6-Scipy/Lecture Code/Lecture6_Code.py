import numpy
import scipy
import matplotlib.pyplot as plt
from scipy import stats
scores = numpy.array([114, 100, 104, 89, 102, 91, 114, 114, 103, 105,
108, 130, 120, 132, 111, 128, 118, 119, 86, 72, 111, 103, 74, 112, 107,
103, 98, 96, 112, 112, 93])
xmean = scipy.mean(scores)
sigma = scipy.std(scores)

print((xmean, sigma ))
n = scipy.size(scores)

print(xmean, xmean - 2.576*sigma /scipy.sqrt(n), xmean + 2.576*sigma / scipy.sqrt(n))
plt.stem(scores)
plt.show()

result=scipy.stats.bayes_mvs(scores)
help(scipy.stats.bayes_mvs)
print(result[0])

print('#',50*"-")
# -----------------------
import scipy.stats
help(scipy.stats)
help(scipy.stats.bayes_mvs)
help(scipy.stats.kurtosis)
numpy.info('random')
print('#',50*"-")
# -----------------------
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
# -----------------------
import scipy.ndimage
import numpy as np
text = scipy.ndimage.imread('image.png')
text = np.mean(text.astype(float)/255,-1)*2-1
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
# -----------------------