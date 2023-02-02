import numpy as np
import statsmodels.api as sm
import pylab as py
# Random data points generated 
data_points = np.random.normal(0, 1, 100)
sm.qqplot(data_points, line='45')
py.show()
