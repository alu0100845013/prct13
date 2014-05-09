#! /usr/bin/python
#! encoding: UTF-8
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-10,10,0.1)
y=4/(1+x**2)
plt.plot(x,y)
plt.show()