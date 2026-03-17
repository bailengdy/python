# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

array = numpy.array(input().split(), float)
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))