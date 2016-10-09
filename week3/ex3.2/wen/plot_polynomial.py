#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as mp
from scipy.optimize import fsolve
#from numpy.polynomial import polynomial as p

x = np.loadtxt('ENyYffaq.txt', delimiter=' ', usecols=(0,))			#load x coodinates as array
y = np.loadtxt('ENyYffaq.txt', delimiter=' ', usecols=(1,))			#load y coodinates as array
#print x
c = np.polyfit(x, y, 3)												#optimize a 3rd degree polynomial's coefficient
#print c[0]
#pow3 = lambda x : c[0]*x**3 + c[1]*x**2 + c[2]*x + c[3]			#diy function
f = np.poly1d(c)													#return the polynomial form by the coefficient
print f		
r = fsolve(f, -20)													#solve root, start from a value of x
print r
##plot config
mp.figure('3rd degree ploynomial')
mp.suptitle('3rd degree ploynomial', fontweight='bold')
mp.xlabel('X')
mp.ylabel('Y')																
mp.plot(x,y,r,'ro')					#plot x on y, root, show red
mp.annotate('0,-1.43463629', xy=(0,-1.43463629), xytext=(2.5,5000),arrowprops=dict(arrowstyle='->'))	# show annotation			
mp.grid()
mp.show()
