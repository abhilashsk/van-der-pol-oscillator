import vanDerPol as vdp
import unittest
import numpy as np
import math

def func1(x,t,mu):
	nx0 = x[1]
	nx1 = x[0]
	res = np.array([nx0, nx1])
	return res

def func2(x,t,mu):
	nx0 = x[1]
	nx1 = -x[0]
	res = np.array([nx0,nx1])
	return res

class TestUM(unittest.TestCase):
	tol = 10**-5
	n = 1000
	ts = np.linspace(0,5.0,1000)

	def setUp(self):
		pass

	#Testing function 1,
	def test_func_one(self):
		res = vdp.integrate(func1,self.ts,[1.0,1.0],(0,))
		err = max([abs(res[i][1] - res[i][0])for i in range(self.n)])
		self.assertLess(err,self.tol)

	#Testing function 2,
	def test_func_two(self):
		res = vdp.integrate(func2,self.ts,[1.0,0.0],(0,))
		err = max([abs(res[i][1]) - abs(math.sqrt(1 - res[i][0]**2))for i in range(self.n)])
		self.assertLess(err,self.tol)

if __name__ == '__main__':
    unittest.main()





