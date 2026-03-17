import numpy

# Solution 1
m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))
matrix = numpy.array(arr)
print(numpy.transpose(matrix))
print(matrix.flatten())

# Solution 2
n, m = map(int, input().split())
matrix = numpy.array([input().split() for _ in range(n)], int)
print(matrix.T)
print(matrix.flatten())