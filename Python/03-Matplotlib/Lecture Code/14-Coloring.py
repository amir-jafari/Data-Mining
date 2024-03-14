import matplotlib.pyplot as plt
import numpy as np
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