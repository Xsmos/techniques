from scipy.stats import kurtosis
import matplotlib.pyplot as plt
import numpy as np

set = [1]*1+[2]*2+[3]*3+[4]*4+[5]*5+[6]*4+[7]*4+[8]*4+[9]*3+[10]*3+[11]*3+[12]*2+[13]*2+[14]*1+[15]*1+[16]*1
print(set)
k = kurtosis(set)
print(k)
plt.hist(set, label = 'kurtosis = {}'.format(k))
plt.legend()
plt.show()
