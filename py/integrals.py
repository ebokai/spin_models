import numpy as np
from scipy.integrate import nquad, tplquad

def f(x1,x2,x3):

	a = 6 * (1 + x3) + 2 * x1 * x2 * (3 + x3)
	b = x2 * x3
	c = 3 + x3 + x1 * (2 + x2 + x2 * x3)
	c = c * c 

	return np.sqrt(a/b)/c

eps = 1e-12

lims = []
ints = []
for lim in np.logspace(0,4,5):
	
	value, error = tplquad(f, eps, lim, eps, lim, eps, lim)
	print(f'lim: {lim:.0f} | V: {value} | D: {error}')


