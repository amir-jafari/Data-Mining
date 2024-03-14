import numpy
import scipy
import matplotlib.pyplot as plt

from scipy.stats import norm
from scipy.stats import ttest_1samp

data = numpy.array([[113,105,130,101,138,118,87,116,75,96,
             122,103,116,107,118,103,111,104,111,89,78,100,89,85,88],
         [137,105,133,108,115,170,103,145,78,107,
              84,148,147,87,166,146,123,135,112,93,76,116,78,101,123]])

dataDiff = data[1,:]-data[0,:]
dataDiff.mean(), dataDiff.std()

plt.rcParams['figure.figsize'] = (15.0, 5.0)
plt.hist(dataDiff)
plt.show()

t_stat,p_value=ttest_1samp(dataDiff,0.0)
print (p_value/2.0)

mean,std=norm.fit(dataDiff)
print(mean,std)
print('#',50*"-")
# -----------------------
from scipy.stats import gaussian_kde

plt.hist(dataDiff, density=1)
x=numpy.linspace(dataDiff.min(),dataDiff.max(),1000)
pdf=norm.pdf(x,mean,std)
plt.plot(x,pdf)


pdf = gaussian_kde(dataDiff)
pdf = pdf.evaluate(x)
plt.hist(dataDiff, density=1)
plt.plot(x,pdf,'k')
plt.show()

plt.hist(dataDiff, density=1)
plt.plot(x,pdf,'k.-',label='Kernel fit')
plt.plot(x,norm.pdf(x,mean,std),'r',label='Normal fit')
plt.legend()
plt.show()
print('#',50*"-")
