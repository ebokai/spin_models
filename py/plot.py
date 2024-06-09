import matplotlib.pyplot as plt 
import numpy as np 
from scipy.special import loggamma as lg

plt.figure(figsize=(10,7))
plt.grid(ls = '--')
plt.tick_params(axis='both', direction='in')
plt.plot([0,7],[0,7], ls = '--')
X = np.linspace(0,8,100)
Y = (X+1)/2 * np.log(np.pi) - lg((X+1)/2)

plt.plot(X,Y/np.log(np.pi), ls = '--')

comps = np.loadtxt('../out/model_complexity_bool_n3_unique_exact.txt', delimiter = ';', dtype = str)
colors = [np.random.uniform(0,1,3) for i in range(9)]
shapes = ['o','^','*','>','^','*','o','^','*']

for i in range(2,9):
	plt.plot(0,-1,marker=shapes[i],ms=15,ls='',c=colors[i],label=rf'$f=${i}')

for i in range(comps.shape[0]):
	model = eval(comps[i,0])
	comp = eval(comps[i,1])
	nf = eval(comps[i,2])
	print(model, comp)

	y = np.log(comp)/np.log(np.pi)

	plt.plot(len(model), y, marker=shapes[nf], c=colors[nf], ms = 15, alpha = 1)

plt.title(r'$n=3,q=2,\mathcal{X}=\{0,1\}$', fontsize = 30)
plt.xlabel(r'$|\mathcal{M}|$', fontsize = 30)
plt.ylabel(r'$\frac{c_{\mathcal{M}}}{\log(\pi)}$', fontsize = 30, rotation = 0, labelpad = 40)
plt.ylim(0,4)
plt.tight_layout()
plt.xticks(fontsize = 25)
plt.yticks(fontsize = 25)
plt.legend(fontsize = 25, ncol = 2)
plt.savefig('../fig/bool_unique_cm_k.png', bbox_inches = 'tight')