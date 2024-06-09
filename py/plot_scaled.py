import matplotlib.pyplot as plt 
import numpy as np 
from scipy.special import loggamma as lg

plt.grid(ls = '--')
plt.tick_params(axis='both', direction='in')

X = np.arange(0,8) 
Y = (X+1)/2 * np.log(np.pi) - lg((X+1)/2)


comps = np.loadtxt('../out/model_complexity_bool_n3_N500000_var12.txt', delimiter = ';', dtype = str)

for i in range(comps.shape[0]):
	model = eval(comps[i,0])
	comp = eval(comps[i,1])
	print(model, comp)

	x = len(model)
	y = np.log(comp)

	plt.plot(x, (y - Y[x])/(X[x]*np.log(np.pi)-Y[x]), '^', c='k', ms = 10, alpha = 0.2)

plt.title(r'$n=3,q=2,\mathcal{X}=\{0,1\}$', fontsize = 20)
plt.xlabel(r'$|\mathcal{M}|$', fontsize = 20)
plt.ylabel(r'$f_C$', fontsize = 20, rotation = 0, labelpad = 20)

plt.tight_layout()
plt.show()