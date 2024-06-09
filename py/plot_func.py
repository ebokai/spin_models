import matplotlib.pyplot as plt 
import numpy as np 
from scipy.special import loggamma as lg



comps = np.loadtxt('../out/model_complexity_bool_n3_unique_exact.txt', delimiter = ';', dtype = str)


m1 = np.array([[1,0],[1,1]])
m2 = np.kron(m1,m1)
m3 = np.kron(m2,m1)

print(m3)

for i in range(comps.shape[0]):

	f = 0

	plt.figure()
	plt.grid(ls = '--')
	plt.ylim(-6.5,16.5)
	model = eval(comps[i,0])
	comp = eval(comps[i,1])
	nf = eval(comps[i,2])

	plt.yticks([-2,0,2,4,6,8,10,12,14])

	

	for kj, j in enumerate(model):
		print(m3[:,j])

		f += m3[:,j]
		plt.bar(np.arange(8), m3[:,j], bottom = 2*j)

	f_str = [x for x in f if x > 0]
	plt.title(f'{model}: {comp} - {f_str} - {nf}')

	plt.bar(np.arange(8), f/len(model), bottom = -2, edgecolor = 'k', color = '#444444')

	obs = []
	for i in range(8):
		ob = 1/8 * np.sum(f * m3[:,i] / len(model))
		obs.append(ob)
		

	plt.bar(np.arange(8), 5*np.array(obs), bottom = -6, color = '#997777')
	plt.savefig(f'../fig/model_{model}_n3_moments.png')
