import numpy
import scipy
import matplotlib.pyplot as plt
from scipy import stats #conda remove scipy --force pip install scipy
scores = numpy.array([114, 100, 104, 89, 102, 91, 114, 114, 103, 105,
108, 130, 120, 132, 111, 128, 118, 119, 86, 72, 111, 103, 74, 112, 107,
103, 98, 96, 112, 112, 93])
xmean = numpy.mean(scores)
sigma = numpy.std(scores)

print((xmean, sigma ))
n = numpy.size(scores)

print(xmean, xmean - 2.576*sigma /numpy.sqrt(n), xmean + 2.576*sigma / numpy.sqrt(n))
plt.stem(scores,use_line_collection= True)
plt.show()

result=scipy.stats.bayes_mvs(scores)
help(scipy.stats.bayes_mvs)
print(result[0])

print('#',50*"-")
# ----------------------