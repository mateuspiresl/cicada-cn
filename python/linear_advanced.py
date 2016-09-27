def multVector(vector, value):
	return [vector[i] * value for i in xrange(len(vector))]

def addVectors(vecA, vecB):
	return [vecA[i] + vecB[i] for i in xrange(len(vecA))]

def subVectors(vecA, vecB):
	return [vecA[i] - vecB[i] for i in xrange(len(vecA))]

def multVectors(vecA, vecB):
	return [vecA[i] * vecB[i] for i in xrange(len(vecA))]

def vectorSum(vector):
	sum = 0
	for i in xrange(len(vector)):
		sum = sum + vector[i]
	return sum

def sumMatrixRow(matrix, row, value):
	matrix[row] = [matrix[row][i] + value for i in xrange(len(matrix))]

def sumMatrixCol(matrix, col, value):
	matrix[col] = [matrix[i][col] + value for i in xrange(len(matrix))]

def multMatrix(matA, matB):
	size = len(matA)
	result = [[0] * size for i in xrange(size)]

	for i in xrange(size):
		aRow = matA[i]

		for j in xrange(size):
			bCol = [matB[row][j] for row in xrange(size)]
			result[i][j] = vectorSum(multVectors(aRow, bCol))

	return result


print "Linear Advanced"

n = int(raw_input("N: "))
matrix = [0] * n

for i in xrange(n):
 	matrix[i] = [float(x) for x in raw_input().split()]

print "Matrix:"
print matrix
print ""

for i in xrange(n):
	firstRows = [[0] * j + [1] + [0] * (n - j - 1) for j in xrange(i)]
	mainRow = [0] * i + [1 / matrix[i][i]] + [0] * (n - i - 1)
	lastRows = [[0] * i + [- matrix[j][i] / matrix[i][i]] + [0] * (j - i - 1) + [1] + [0] * (n - j - 1) for j in xrange(i + 1, n)]
	aux = firstRows + [mainRow] + lastRows
	print 'Aux:'
	print aux
	print ""

	matrix = multMatrix(aux, matrix)
	print 'Matrix:'
	print matrix
	print ""
	# print '\non ' + str(i)
	# print matrix
	
	for j in xrange(i + 1, n):
		# print '\non ' + str(i) + ', ' + str(j)
		# print '\t' + str(matrix[j]) + ' -'
		# print '\t(' + str(matrix[i]) + ' * ' + str(matrix[j][i]) + ') = ' + str(multVector(matrix[i], matrix[j][i]))
		matrix[j] = subVectors(matrix[j], multVector(matrix[i], matrix[j][i]))
		# print matrix

print matrix