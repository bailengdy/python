# Brute Force
# Python Syntax Exercise
def image_smoother(self, img):
    m, n = len(img), len(img[0])
    res = [[0] * n for _ in range(m)]

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for i in range(m):
        for j in range(n):
            total = 0
            count = 0

            for dx, dy in directions:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n:
                    total += img[x][y]
                    count += 1

            res[i][j] = total // count

    return res


# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(image_smoother([[1,1,1],[1,0,1],[1,1,1]]))
# [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
print(image_smoother([[100,200,100],[200,50,200],[100,200,100]]))