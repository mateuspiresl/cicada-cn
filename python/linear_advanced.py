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

def multMatrixs(matA, matB):
	size = len(matA)
	result = [[0] * size] * size

	for i in range(size):
		aRow = matA[i]

		for j in range(size):
			bCol = [matB[row][j] for row in xrange(size)]
			result[i][j] = vectorSum(multVectors(aRow, bCol))

	return result


n = int(raw_input())
matrix = [0] * n

for i in xrange(n):
 	matrix[i] = [float(x) for x in raw_input().split()]

print matrix

for i in xrange(n):
	auxRow = [0] * i + [- 1 / matrix[i][i]] + [0] * (n - i - 1)
	aux = [[0] * n] * i + [auxRow] * (n - i)
	print 'aux'
	print aux

	matrix = multMatrixs(matrix, aux)
	print 'matrix'
	print matrix
	# print '\non ' + str(i)
	# print matrix
	
	for j in xrange(i + 1, n):
		# print '\non ' + str(i) + ', ' + str(j)
		# print '\t' + str(matrix[j]) + ' -'
		# print '\t(' + str(matrix[i]) + ' * ' + str(matrix[j][i]) + ') = ' + str(multVector(matrix[i], matrix[j][i]))
		matrix[j] = subVectors(matrix[j], multVector(matrix[i], matrix[j][i]))
		# print matrix

print matrix