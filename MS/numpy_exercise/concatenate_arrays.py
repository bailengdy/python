import numpy



m, n, p = map(int, input().split())
arr1 = numpy.array([input().split() for _ in range(m)], int)
arr2 = numpy.array([input().split() for _ in range(n)], int)
# axis 0 ↓
# axis 1 →
print(numpy.concatenate((arr1, arr2), axis = 0))
