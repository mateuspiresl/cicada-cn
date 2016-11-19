def internProduct(vecA, vecB):
	result = 0
	for i in xrange(len(vecA)):
		result += vecA[i] * vecB[i]
	return result

def matrixProduct(matA, matB):
	rows = len(matB)
	cols = len(matB[0])

	result = [[0] * cols for i in xrange(rows)]

	for i in xrange(rows):
		aRow = matA[i]

		for j in xrange(cols):
			bCol = [matB[row][j] for row in xrange(rows)]
			result[i][j] = internProduct(aRow, bCol)

	return result

def printMatrix(matrix):
	for i in xrange(len(matrix)):
		print matrix[i]

def trangularization(matrix):
	auxs = []
	result = matrix

	for i in xrange(n):
		# Builds first rows of identity matrix (if the first row is not the main row)
		firstRows = [[0] * j + [1] + [0] * (n - j - 1) for j in xrange(i)]
		# Builds working row, needed to turn main cell to 1
		mainRow = [0] * i + [1] + [0] * (n - i - 1)
		# Builds last rows of identity matrix, turns main cells to 0 and identity cells
		#			first 0s   turns main col to 0				0s until identity	identity   last 0s
		lastRows = [[0] * i +  [- result[j][i] / result[i][i]] + [0] * (j - i - 1) + [1] + 	   [0] * (n - j - 1) for j in xrange(i + 1, n)]
		
		aux = firstRows + [mainRow] + lastRows
		auxs.append(aux)

		#print '\nOP:'
		#printMatrix(aux)
		#print '*'
		#printMatrix(result)

		result = matrixProduct(aux, result)

		#print '='
		#printMatrix(result)

	return result, auxs

def solveTriangularizedLinearSystem(matrix):
	#print '\nCalculating vars:'

	vec = [float(0)] * len(matrix)
	#print 'vec: ' + str(vec) + '\n'

	for i in xrange(len(matrix) - 1, -1, -1):
		#print 'Current: ' + str(i)

		value = matrix[i][len(matrix)]
		#print '\tvalue: ' + str(value)
		
		for j in xrange(i + 1, len(matrix)):
			#print '\t\tCalc for ' + str(j)
			
			value = value - (vec[j] * matrix[i][j])
			#print '\t\tvalue: ' + str(value)

		vec[i] = value / matrix[i][i]
		#print '\tvec[' + str(i) + ']: ' + str(vec[i])

	return vec


if __name__ == "__main__":
	print "Linear-Advanced"

	n = int(raw_input("N: "))
	matrix = [0] * n

	for i in xrange(n):
	 	matrix[i] = [float(x) for x in raw_input().split()]

	result, auxs = trangularization(matrix)
	auxsMult = auxs[0]

	for i in xrange(1, len(auxs)):
		auxsMult = matrixProduct(auxs[i], auxsMult)
	
	vec = solveTriangularizedLinearSystem(result)

	print "\n\nRESULT:"
	print "\nMatrix:"
	printMatrix(matrix)
	print "\nResult"
	printMatrix(result)
	print "\nP:"
	printMatrix(auxsMult)
	print "\nP x Matrix:"
	printMatrix(matrixProduct(auxsMult, matrix))
	print '\nVars:'
	print vec