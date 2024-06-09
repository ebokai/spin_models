import sm
import numpy as np
from itertools import combinations
from helper import generate_unique_models, generate_binary_basis

n = 3
N = 250000
s = 4 # standard deviation of proposal distribution

for k in range(1,8):
	basis = generate_binary_basis(n)
	models, int_models, strings = generate_unique_models(basis, k)
	for model, vecs, string in zip(int_models, models, strings):
		
		model_instance = sm.SpinModel(n,list(model))

		nf = model_instance.unique_energies()




		print('\n')
		print('model:', list(model))
		print('model id:', string)
		print('n freq:', nf)
		print('opsum:', np.sum(vecs))



		comp = model_instance.complexity(N = N, std = s, verbose = False)

		out_str = f'{list(model)};{comp:.6f};{nf};{np.sum(vecs)};{string}\n'

		with open(f'../out/model_complexity_bool_n{n}_unique_{N}_std{s}.txt', 'a+') as f:
			f.write(out_str)
