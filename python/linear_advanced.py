def internProduct(vecA, vecB):
	result = 0
	for i in xrange(len(vecA)):
		result += vecA[i] * vecB[i]
	return result

def matrixProduct(matA, matB):
	size = len(matA)
	result = [[0] * size for i in xrange(size)]

	for i in xrange(size):
		aRow = matA[i]

		for j in xrange(size):
			bCol = [matB[row][j] for row in xrange(size)]
			result[i][j] = internProduct(aRow, bCol)

	return result

def printMatrix(matrix):
	for i in xrange(len(matrix)):
		print matrix[i]


if __name__ == "__main__":
	print "Linear-Advanced"

	n = int(raw_input("N: "))
	matrix = [0] * n

	for i in xrange(n):
	 	matrix[i] = [float(x) for x in raw_input().split()]

	b = [float(x) for x in raw_input().split()]
	print 'b: ' + str(b)
	
	auxs = []
	result = matrix

	for i in xrange(n):
		# Builds first rows of identity matrix (if the first row is not the main row)
		firstRows = [[0] * j + [1] + [0] * (n - j - 1) for j in xrange(i)]
		# Builds working row, needed to turn main cell to 1
		mainRow = [0] * i + [1 / result[i][i]] + [0] * (n - i - 1)
		# Builds last rows of identity matrix, turns main cells to 0 and identity cells
		#			first 0s   turns main col to 0				0s until identity	identity   last 0s
		lastRows = [[0] * i +  [- result[j][i] / result[i][i]] + [0] * (j - i - 1) + [1] + 	   [0] * (n - j - 1) for j in xrange(i + 1, n)]
		
		aux = firstRows + [mainRow] + lastRows
		auxs.append(aux)

		result = matrixProduct(aux, result)

	auxsMult = auxs[0]

	for i in xrange(1, len(auxs)):
		auxsMult = matrixProduct(auxs[i], auxsMult)

	print '\n'

	vec = [float(0)] * len(matrix)
	print 'vec: ' + str(vec) + '\n'

	for i in xrange(len(matrix) - 1, -1, -1):
		print 'Current: ' + str(i)

		value = b[i]
		print '\tvalue: ' + str(value)
		
		for j in xrange(i + 1, len(matrix)):
			print '\t\tCalc for ' + str(j)
			
			value = value - (vec[j] * matrix[i][j])
			print '\t\tvalue: ' + str(value)

		vec[i] = value / matrix[i][i]
		print '\tvec[' + str(i) + ']: ' + str(vec[i])



	print "\n\nRESULT:"
	print "\nMatrix:"
	printMatrix(matrix)
	print "\nResult"
	printMatrix(result)
	print "\nP:"
	printMatrix(auxsMult)
	print "\nP x Matrix:"
	printMatrix(matrixProduct(auxsMult, matrix))