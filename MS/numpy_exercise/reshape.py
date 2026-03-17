import numpy


# Solution 1
array = numpy.array(input().split(), int)
array.shape = (3, 3)
print(array)

# Solution 2
arr = numpy.array(input().split(), int)
print(numpy.reshape(arr, (3, 3)))