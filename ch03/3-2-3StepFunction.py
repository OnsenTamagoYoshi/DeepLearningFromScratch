# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 01:44:54 2017

@author: win8_VM_user
"""

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #y軸の範囲を指定
plt.show()
