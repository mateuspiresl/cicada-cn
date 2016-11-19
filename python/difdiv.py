import sys
import math

def calc_div(dom, img, a, b):
	return (img[a + 1] - img[a]) / (dom[b] - dom[a])

if __name__ == "__main__":
	size = int(input())
	print 'Size: ' + str(size) + ' (' + str(size * 2) + ')\n'

	dom = []
	divs = [[]]

	for i in xrange(2, size * 2 + 2, 2):
		couple = raw_input().split()

		dom.append(float(couple[0]))
		divs[0].append(float(couple[1]))

	print 'dom: ' + str(dom)
	print 'img: ' + str(divs[0]) + '\n'

	for i in xrange(1, size):
		divs.append([])

		for j in xrange(len(divs[i - 1]) - 1):
			divs[i].append(calc_div(dom, divs[i - 1], j, j + i))

		print str(i) + 'o div: ' + str(divs[len(divs) - 1])

	x = input()
	result = 0

	for i in xrange(size):
		val = divs[i][0]

		for j in xrange(i):
			val = val * (x - dom[j])

		result = result + val

	print '\n' + str(x) + '  ->  ' + str(result)