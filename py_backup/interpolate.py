import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x_raw = np.arange(0,20)
y_raw = np.cos(x_raw)

x_fit = np.arange(-2,22,0.1)
y_numpy1 = np.interp(x_fit, x_raw, y_raw)
y_scipy1 = interp1d(x_raw,y_raw, kind='slinear', fill_value = 'extrapolate')(x_fit)
y_scipy3 = interp1d(x_raw,y_raw, kind='cubic', fill_value = 'extrapolate')(x_fit)

plt.scatter(x_raw, y_raw, label = 'raw')
plt.plot(x_fit, y_numpy1, label = 'y_numpy1')
plt.plot(x_fit, y_scipy1, label = 'y_scipy1', linestyle = '--')
plt.plot(x_fit, y_scipy3, label = 'y_scipy3')

plt.legend()
plt.show()