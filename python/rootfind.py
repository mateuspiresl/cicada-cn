# -*- coding: utf-8 -*-

###	Mateus Pires Lustosa
###	José Ademir Queiroga
#	mateusplpl@gmail.com
#
#	Implementações de métodos para encontrar raízes de funções
#		- Método para encontrar intervalo
#		- Método da bisseção
#		- Método de Newton
#		- Método da aproximação linear
#
#	Uso: func [max_iter [z [deriv [initial_x] ] ] ]
#		func - função, ex.: "x**3 - 10".
#		max_iter - número máximo de iterações. Valor padrão: 40.
#		z - parâmetro para encontrar intervalo. Valor padrão: 0.
#		deriv - derivada da função func. Necessário para o método de Newton.
#		initial_x - valor inicial do x para busca da raíz. Valor padrão:
#			intervalo direito.

import sys
from math import *
import re

class root:
	Accuracy = 10e-15
	Aureo = 2 / (sqrt(5) - 1)
	IterMax = 60
	ErrorCodes = { -1: "Fail", 0: "Success", 1: "Tolerated", 2: "Maximum number of iterations" }

	@staticmethod
	def use(func, x):
		if type(func) == str:
			return eval(func)
		else:
			return func(x)

	@staticmethod
	def processFunc(func):
		func = re.sub("sen", "sin", func)
		func = re.sub("tan", "tg", func)
		func = re.sub(r"\^", r"**", func)
		func = re.sub(r"(cos|sin|tan|acos|asin|atan|log|exp|sqrt|pow|ln) \(", r"\1(", func)
		func = re.sub(r"(cos|sin|tan|acos|asin|atan|log|exp|sqrt|pow|ln) ([\dx\+\-\*\/]+)", r"\1(\2)", func)
		func = re.sub(r"ln ?\(([\dx \+\-\*\/]+)\)", r"log(\1, e)", func)
		return func

	#	Finds interval
	#	Parameters:
	#		func - function
	#		maxIter - maximum number of iterations
	#		z - feed
	#	Return:
	#		a - Left interval
	#		fa - func(a)
	#		b - Right interval
	#		fb - func(b)
	#		i - Number of iterations
	#		errorCode:
	#			-1 - Fail
	#			0 - Success
	#			1 - Maximum number of iterations
	@staticmethod
	def findInterval(func, maxIter, z):
		if z == 0:
			a = -0.05
			b = 0.05
		else:
			a = 0.95 * z
			b = 1.05 * z

		fa = root.use(func, a)
		fb = root.use(func, b)
		i = 0

		while fa * fb > 0 and i < maxIter:
			if abs(fa) < abs(fb):
				a = a - root.Aureo * (b - a)
				fa = root.use(func, a)
			else:
				b = b + root.Aureo * (b - a)
				fb = root.use(func, b)

			i = i + 1

		if fa * fb < 0:
			if i == maxIter: errorCode = 1
			else: errorCode = 0
		else: errorCode = -1

		return a, fa, b, fb, i, errorCode

	#	Finds a root using the bissection method
	#	Parameters:
	#		func - Function
	#		a - minimum value
	#		b - maximum value
	#		tolerance - allowed distance from 0 to be considered valid
	#		maxIter - maximum number of iterations
	#	Return:
	#		errorCode:
	#			-1 - Fail
	#			0 - Success
	#			1 - Tolerated
	#			2 - Maximum iterations
	@staticmethod
	def bissection(func, a, b, tolerance, maxIter):
		fa = root.use(func, a)
		fb = root.use(func, b)

		xVar = abs(b - a) / 2
		x = a + xVar
		fx = root.use(func, x)

		i = 0

		while xVar > tolerance and abs(fx) > tolerance and i < maxIter:
			if fx * fa < 0:
				b = x
				fb = root.use(func, b)
			else:
				a = x
				fa = root.use(func, a)

			xVar = xVar / 2
			x = a + xVar
			fx = root.use(func, x)
			i = i + 1

		errorCode = -1
		
		if fa * fb < 0:
			if fx == 0:
				errorCode = 0
			elif xVar <= tolerance or abs(fx) <= tolerance:
				errorCode = 1
			elif i == maxIter:
				errorCode = 2

		return x, fx, i, errorCode

	#	Finds a root using the bissection method
	#	Parameters:
	#		func - Function
	#		deriv - Derivate of the function
	#		x - starting x
	#		tolerance - allowed distance from 0 to be considered valid
	#		maxIter - maximum number of iterations
	#	Return
	#		errorCode:
	#			-1 - Fail
	#			0 - Success
	#			1 - Tolerated
	#			2 - Maximum iterations
	@staticmethod
	def newton(func, deriv, x, tolerance, maxIter):
		f = root.use(func, x)
		i = 0

		while abs(f) > tolerance and i < maxIter:
			df = root.use(deriv, x)

			x = x - float(f) / df
			f = root.use(func, x)
			i = i + 1

		if f == 0:
			errorCode = 0
		elif abs(f) <= tolerance:
			errorCode = 1
		elif i == maxIter:
			errorCode = 2
		else:
			errorCode = -1

		return x, f, i, errorCode

	#	Finds a root using the linear approximation method
	#	Parameters:
	#		func - Function
	#		a - left interval
	#		b - right interval
	#		tolerance - allowed distance from 0 to be considered valid
	#		maxIter - maximum number of iterations
	#	Return
	#		errorCode:
	#			-1 - Fail
	#			0 - Success
	#			1 - Tolerated
	#			2 - Maximum iterations
	@staticmethod
	def linearApprox(func, a, b, tolerance, maxIter):
		fa = root.use(func, a)
		fb = root.use(func, b)
		i = 0

		while i < maxIter:
			i = i + 1

			x = b - fb * ((b - a) / (fb - fa))
			fx = root.use(func, x)

			if abs(fx) <= tolerance: break

			if fa * fx < 0:
				a = x
				fa = fx
			else:
				b = x
				fb = fx

		if fx == 0:
			errorCode = 0
		elif abs(fx) <= tolerance:
			errorCode = 1
		elif i == maxIter:
			errorCode = 2
		else:
			errorCode = -1

		return x, fx, i, errorCode


def printResult(name, result):
	x, fx, i, errorCode = result

	print "\n" + name + ":"
	print "\tStatus\t\t\t" + root.ErrorCodes[errorCode]
	print "\tNumber of iterations\t" + str(i)
	print "\tx\t\t\t" + str(x)
	print "\tf(x)\t\t\t" + str(fx)

#	root.use: func [maxIter [z [deriv [initialX] ] ] ]
if __name__ == "__main__":
	if len(sys.argv) <= 1:
		print "Use: func [maxIter(=40) [z(=0) [deriv [initialX] ] ]"
	else:
		print "\nFunction:"
		func = sys.argv[1]
		print "\t" + func

		processedFunc = root.processFunc(func)
		if func != processedFunc:
			func = processedFunc
			print "Processed:"
			print "\t" + func

		if len(sys.argv) > 4:
			print "\nDerived:"
			deriv = sys.argv[4]
			print "\t" + deriv

			processedFunc = root.processFunc(deriv)
			if deriv != processedFunc:
				deriv = processedFunc
				print "Processed:"
				print "\t" + deriv

		if len(sys.argv) > 2: maxIter = eval(sys.argv[2])
		else: maxIter = root.IterMax

		if len(sys.argv) > 3: z = eval(sys.argv[3])
		else: z = 0
		
		interval = root.findInterval(func, maxIter, z)
		a, fa, b, fb, i, errorCode = interval
		print "\nInterval:"
		print "\tStatus\t\t\t" + root.ErrorCodes[errorCode]
		print "\tNumber of iterations\t" + str(i)
		print "\ta\t\t\t" + str(a)
		print "\tb\t\t\t" + str(b)
		print "\tf(a)\t\t\t" + str(fa)
		print "\tf(b)\t\t\t" + str(fb)

		result = root.bissection(func, a, b, root.Accuracy, maxIter)
		printResult("Bissection", result)

		result = root.linearApprox(func, a, b, root.Accuracy, maxIter)
		printResult("Linear Approximation", result)

		if len(sys.argv) > 4:
			if len(sys.argv) > 5:
				initialX = eval(sys.argv[5])
			else:
				initialX = b

			result = root.newton(func, deriv, initialX, root.Accuracy, maxIter)
			printResult("Newton", result)