
import math

class Matrix:
	Superior = 1
	Inferior = -1
	ArgumentException = Exception('The argument must be a matrix')
	NotTriangularizedException = Exception('Matrix must be triangularized for this process')

	def __init__(self, matrix):
		if type(matrix) is not list:
			raise Matrix.ArgumentException

		for vec in matrix:
			if type(vec) is not list:
				raise Matrix.ArgumentException

		self.data = matrix
		self.triangularization = None

	@staticmethod
	def ofSize(rows, cols):
		data = [[0] * cols for r in xrange(rows)]
		return Matrix(data)

	@staticmethod
	def internProduct(vecA, vecB):
		result = 0
		for i in xrange(len(vecA)):
			result += vecA[i] * vecB[i]
		return result

	@staticmethod
	def product(matA, matB):
		rows = len(matB.data)
		cols = len(matB.data[0])

		result = [[0] * cols for i in xrange(rows)]

		for i in xrange(rows):
			aRow = matA.data[i]

			for j in xrange(cols):
				bCol = [matB.data[row][j] for row in xrange(rows)]
				result[i][j] = Matrix.internProduct(aRow, bCol)

		result = Matrix(result)

		if matA.triangularization == matB.triangularization:
			result.triangularization = matA.triangularization

		return result

	def display(self, tab = ''):
		for i in xrange(len(self.data)):
			print tab + str(self.data[i])

	def trangularize(self, triangularization):
		auxs = []
		result = self
		n = len(self.data)

		if triangularization == Matrix.Superior:
			for i in xrange(n):
				# Builds first rows of identity matrix (if the first row is not the main row)
				firstRows = [[0] * j + [1] + [0] * (n - j - 1) for j in xrange(i + 1)]
				# Builds last rows of identity matrix, turns main cells to 0 and identity cells
				#			first 0s   turns main col to 0							0s until identity	identity   last 0s
				lastRows = [[0] * i +  [- result.data[j][i] / result.data[i][i]] +	[0] * (j - i - 1) +	[1] + 	   [0] * (n - j - 1) for j in xrange(i + 1, n)]
				
				aux = Matrix(firstRows + lastRows)
				auxs.append(aux)

				result = Matrix.product(aux, result)

		elif triangularization == Matrix.Inferior:
			for i in xrange(n - 1, -1, -1):
				# Builds last rows of identity matrix, turns main cells to 0 and identity cells
				#			first 0s   turns main col to 0							0s until identity	identity   last 0s
				lastRows = [[0] * i +  [- result.data[j][i] / result.data[i][i]] + [0] * (j - i - 1) + [1] + 	   [0] * (n - j - 1) for j in xrange(i + 1, n)]
				# Builds first rows of identity matrix (if the first row is not the main row)
				firstRows = [[0] * (n - j - 1) + [1] + [0] * j for j in xrange(i + 1)]
				
				aux = Matrix(firstRows + lastRows)
				auxs.append(aux)

				result = Matrix.product(aux, result)

		result.triangularization = triangularization
		print 'trian: ' + str(result.triangularization)
		return result, auxs

	def solveTriangularized(self):
		if self.triangularization == None:
			raise Matrix.NotTriangularizedException;

		#print '\nCalculating vars:'

		vec = [float(0)] * len(self.data)
		#print 'vec: ' + str(vec) + '\n'

		for i in xrange(len(self.data) - 1, -1, -1):
			#print 'Current: ' + str(i)

			value = self.data[i][len(self.data)]
			#print '\tvalue: ' + str(value)
			
			for j in xrange(i + 1, len(self.data)):
				#print '\t\tCalc for ' + str(j)
				
				value = value - (vec[j] * self.data[i][j])
				#print '\t\tvalue: ' + str(value)

			vec[i] = value / self.data[i][i]
			#print '\tvec[' + str(i) + ']: ' + str(vec[i])

		return vec

	def cholesk(self):
		size = len(self.data)

		result = Matrix.ofSize(size, size)
		result.data[0][0] = math.sqrt(self.data[0][0])

		for i in xrange(1, size):
			result.data[i][0] = self.data[i][0] / result.data[0][0]

		for i in (1, size - 2):
			total = 0
			for j in xrange(i):
				total = total + result.data[i][j] ** 2

			result.data[i][i] = math.sqrt(self.data[i][i] - total)

			for j in xrange(i + 1, size):
				total = 0
				for k in xrange(i):
					total = total + result.data[i][k] * result.data[j][k]

				result.data[j][i] = (self.data[i][j] - total) / result.data[i][i]

		total = 0
		for i in xrange(size - 1):
			total = total + result.data[size - 1][i] ** 2

		result.data[size - 1][size - 1] = math.sqrt(self.data[size - 1][size - 1] - total)

		result.triangularization = Matrix.Inferior
		return result

	def inverse(self):
		if self.triangularization == None:
			raise Matrix.NotTriangularizedException;

		size = len(self.data)
		inverse = Matrix.ofSize(size, size)

		for i in xrange(size):
			for j in xrange(i, size):
				inverse.data[i][j] = self.data[j][i]

		return inverse

	def det(self):
		if self.triangularization == None:
			raise Matrix.NotTriangularizedException;

		result = 1
		for i in xrange(len(self.data)):
			result = result * self.data[i][i]

		return result


if __name__ == "__main__":
	n = int(raw_input())
	matrix = [0] * n

	for i in xrange(n):
	 	matrix[i] = [float(x) for x in raw_input().split()]

	matrix = Matrix(matrix)

	result, auxs = matrix.trangularize(Matrix.Superior)
	auxsMult = auxs[0]

	for i in xrange(1, len(auxs)):
		auxsMult = Matrix.product(auxs[i], auxsMult)

	vec = result.solveTriangularized()

	print "Matrix:"
	matrix.display('\t')
	print "\nResult"
	result.display('\t')
	print "\nP:"
	auxsMult.display('\t')
	print "\nP x Matrix = Result:"
	Matrix.product(auxsMult, matrix).display('\t')
	print '\nVars:'
	print vec

	print '\nCholesk - L*L^-1:'
	choleskResult = matrix.cholesk()
	Matrix.product(choleskResult, choleskResult.inverse()).display('\t')

	print '\nDet: ' + str(choleskResult.det() ** 2)