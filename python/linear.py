def multVector(vector, value):
	return [vector[i] * value for i in xrange(len(vector))]

def subVectors(vecA, vecB):
	return [vecA[i] - vecB[i] for i in xrange(len(vecA))]


n = int(raw_input())
matrix = [0] * n

for i in xrange(n):
 	matrix[i] = [float(x) for x in raw_input().split()]

print matrix

for i in xrange(n):
	matrix[i] = multVector(matrix[i], 1 / matrix[i][i])
	# print '\non ' + str(i)
	# print matrix
	
	for j in xrange(i + 1, n):
		# print '\non ' + str(i) + ', ' + str(j)
		# print '\t' + str(matrix[j]) + ' -'
		# print '\t(' + str(matrix[i]) + ' * ' + str(matrix[j][i]) + ') = ' + str(multVector(matrix[i], matrix[j][i]))
		matrix[j] = subVectors(matrix[j], multVector(matrix[i], matrix[j][i]))
		# print matrix

print matrix