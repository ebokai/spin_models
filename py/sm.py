import numpy as np
import tools
import time

class SpinModel():

	def __init__(self, n, model):

		self.n = n
		self.model = model
		self.parameters = np.array([0. for _ in range(2**n)])

		# construct hadamard matrix
		self.init_matrix()

	def init_matrix(self):
		self.hadamard = tools.hadamard_matrix(self.n)

	# def calculate_moments(self):

	# 	u = np.exp(tools.fwht(self.parameters))
	# 	z = np.sum(u)
	# 	p = u/z 

	# 	return tools.fwht(p)

	def calculate_moments(self):

		p = self.calculate_p()

		return self.hadamard.T @ p

	def calculate_p(self):

		u = np.exp(self.hadamard @ self.parameters)
		z = np.sum(u)
		p = u/z 

		return p


	def unique_energies(self):

		dim = len(self.model)
		self.parameters[self.model] = np.random.uniform(-2,2,dim)

		p = self.calculate_p()

		pr = np.round(p, 5)
		u = np.unique(pr)

		return len(u)



	def fisher_information(self, parameters = None):

		if parameters is not None:
			self.parameters[self.model] = parameters

		moments = self.calculate_moments()

		# Fij = <fifj> - <fi><fj>

		indices_xor = np.array([[o1 | o2 for o1 in self.model] for o2 in self.model])

		moments_prod = np.outer(moments[self.model], moments[self.model])
		moments_xor = moments[indices_xor]

		fij = moments_xor - moments_prod

		return fij

	def fisher_determinant(self, parameters = None):

		fij = self.fisher_information(parameters)

		return np.sqrt(np.abs(np.linalg.det(fij)))

	def complexity(self, N = 100000, std = 5, verbose = True):

		integral = 0

		dim = len(self.model)
		var = std**2

		v_norm = (2 * np.pi * var) ** (dim/2)

		start = time.perf_counter()

		pf = (1 / np.sqrt((2 * np.pi * var) ** dim))


		for i in range(N):

			pars = np.random.normal(0, std, dim)
			p_x = pf * np.exp(-0.5 * np.sum(pars ** 2) / var)
			det = self.fisher_determinant(pars)
			integral += det / p_x

			if ((i + 1) % 10000) == 0 and verbose:
				print(f'it: {i+1}, integral: {integral/(i+1):.4f}')

		end = time.perf_counter()

		result = integral/N

		print(f'time elapsed: {end - start:.1f} sec')
		print(f'integral: {result:.6f}')
		print(f'pi power: {np.log(result)/np.log(np.pi):.6f}')
		return result


