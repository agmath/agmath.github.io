from random import *
import numpy as np
import sympy

seed(1)

N = 100
x = []
y = []
for i in range(N):
    x.append(2*random())

x = np.array(x)
x = x - np.mean(x)
y = np.multiply(2,x)

A = sympy.Matrix([x,y])
