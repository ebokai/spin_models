import matplotlib.pyplot as plt 
import numpy as np 
from scipy.special import loggamma as lg


plt.figure(figsize=(9,7))
plt.grid(ls = '--')
plt.tick_params(axis='both', direction='in')
# plt.plot([0,7],[0,7], ls = '--')
X = np.linspace(0,8,100)
Y = (X)/2 * np.log(np.pi) - lg((X)/2)

plt.plot(X,Y/np.log(np.pi), ls = '--')

comps = np.loadtxt('../out/model_complexity_bool_n3_unique_exact.txt', delimiter = ';', dtype = str)


colors = [np.random.uniform(0,1,3) for i in range(8)]
shapes = ['o','^','*','>','^','*','o','^','*']

for i in range(8):
	plt.plot(0,-1,marker=shapes[i],ms=10,ls='',c=colors[i],label=f'K={i}')

for i in range(comps.shape[0]):
	model = eval(comps[i,0])
	comp = eval(comps[i,1])
	nf = eval(comps[i,2])
	print(model, comp, nf)

	y = np.log(comp)/np.log(np.pi)

	plt.plot(nf, y, marker = shapes[len(model)], c=colors[len(model)], ms = 15, alpha = 1)

plt.title(r'$n=3,q=2,\mathcal{X}=\{0,1\}$', fontsize = 20)
plt.xlabel(r'$f$', fontsize = 20)
plt.ylabel(r'$\frac{c_{\mathcal{M}}}{\log(\pi)}$', fontsize = 20, rotation = 0, labelpad = 20)
plt.ylim(0,4)
plt.legend()
plt.tight_layout()
plt.show()