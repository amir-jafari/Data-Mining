import matplotlib.pyplot as plt
import numpy as np
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
x16 = np.linspace(-4, 4, 1000)
y16 = .25 * (x16 + 4) * (x16 + 1) * (x16 - 2)
plt.title('A polynomial' r'$f(x)=\frac{1}{4}(x+4)(x+1)(x-2)$')
plt.plot(x16, y16, c = 'k')
plt.show()
print('#',50*"-")