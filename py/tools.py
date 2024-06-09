import numpy as np 
from numba import njit

def hadamard_matrix(n):

	f = np.array([[1,0],[1,1]])

	if n == 1:
		return f 
	else:
		return np.kron(f, hadamard_matrix(n - 1))

@njit(fastmath=True)
def fwht(u):
	v = u.copy()
	h = 1 
	lv = len(v)
	while h < lv:
		for i in range(0, lv, h * 2):
			for j in range(i, i + h):
				x = v[j]
				y = v[j + h]
				v[j] = x + y 
				v[j + h] = x - y 
		h *= 2
	return v