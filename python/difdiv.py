import sys
import math

def calc_div(dom, img, a, b):
	return (img[a + 1] - img[a]) / (dom[b] - dom[a])

if __name__ == "__main__" and len(sys.argv) > 2:
	size = int(sys.argv[1])

	print 'Arg number: ' + str(len(sys.argv))
	print 'Size: ' + str(size) + ' (' + str(size * 2) + ')\n'

	if len(sys.argv) - 2 < size * 2:
		print 'Wrong argument number'
	else:
		dom = []
		divs = [[]]

		for i in xrange(2, size * 2 + 2, 2):
			dom.append(float(sys.argv[i]))
			divs[0].append(float(sys.argv[i + 1]))

		print 'dom: ' + str(dom)
		print 'img: ' + str(divs[0]) + '\n'

		for i in xrange(1, size):
			divs.append([])

			for j in xrange(len(divs[i - 1]) - 1):
				divs[i].append(calc_div(dom, divs[i - 1], j, j + i))

			print str(i) + 'o div: ' + str(divs[len(divs) - 1])