import sys
import math

accuracy = 10e-14

def use(func, arg):
	x = arg
	return eval(func)

def roots_bi(func, a, b, n):
	middle = a + (b - a) / 2
	if n == 0 or abs(use(func, middle)) < accuracy:
		#if use(func, middle) < 10e-12:
			return middle, n
		#else:
		#	raise Exception('nao ha raiz no intervalo')

	if use(func, middle) * use(func, b) < 0:
		return roots_bi(func, middle, b, n - 1)
	else:
		return roots_bi(func, a, middle, n - 1)

def roots_newton(func, deriv, a, b, n):
	fa = use(func, a)
	if fa == 0: return a, n
	fb = use(func, b)
	if fb == 0: return b, n

	if a == b: raise Exception('nao ha raiz no intervalo')

	da = use(deriv, a)
	if da == 0: raise Exception('ponto critico')

	if (a < b and da * fa < 0) or (a > b and da * fa > 0):
		if abs(fa / da) < accuracy: return a, n

		x = a - fa / da

		if abs(x - b) >= abs(a - b):
			raise Exception('nao ha raiz no intervalo')

		if (a < b and x < b) or (a > b and x > b):
			return roots_newton(func, deriv, x, b, n - 1)
		
		#print "swap"
		return roots_newton(func, deriv, b, a, n)
	else:
		raise Exception('ha ponto critico ou nao ha raiz no intervalo')

#def eq(x): return x * x + 5 * x + 1.7
#def eq_deriv(x): return 2 * x + 5
#a = -2.0
#b = 2.0

if __name__ == "__main__" and len(sys.argv) > 3:
	a = sys.argv[1]
	b = sys.argv[2]
	userEq = sys.argv[3]

	print "roots_bi"
	try:
		r, n = roots_bi(userEq, eval(a), eval(b), 60)
		print str(r) + " (" + str(60 - n) + ")"
	except Exception as exc:
		print exc


	if len(sys.argv) > 4:
		userEqDeriv = sys.argv[4]

		print "roots_newton"
		try:
			r, n = roots_newton(userEq, userEqDeriv, eval(a), eval(b), 60)
			print str(r) + " (" + str(60 - n) + ")"
		except Exception as exc:
			print exc