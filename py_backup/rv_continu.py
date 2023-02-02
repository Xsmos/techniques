from scipy.stats import rv_continuous
import numpy as np
import matplotlib.pyplot as plt

class TriangleDistribution(rv_continuous):
    def _pdf(self, x):
        y = np.zeros(np.size(x))
        
        if np.size(x) == 1:
            if 0<=x<=1:
                y = 1 - x
            elif -1<=x<=0:
                y = 1 + x
        else:
            i = np.where((0 <= x)&(x <= 1))
            y[i] = 1 - x[i]

            i = np.where((-1 <= x)&(x <= 0))
            y[i] = 1 + x[i]
        
        return y

triangle = TriangleDistribution(a = -2, b = 2)
x = np.arange(-2,2)
y = triangle.pdf(x)

samples = triangle.rvs(size = 1000) # take 1000 random numbers from this distribution

plt.plot(x, y, label = 'triangle pdf')
plt.hist(samples, bins = 20, density = True, label = 'samples')
plt.xlabel('x')
plt.ylabel('PDF and samples')
plt.legend()
plt.show()