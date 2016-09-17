#!/usr/bin/python

import numpy as np

A = np.loadtxt('XAhwshXe.txt', delimiter=',', usecols=(0,1,2))
b = np.loadtxt('XAhwshXe.txt', delimiter=',', usecols=(3,))

result = np.linalg.solve(A,b)

print result





