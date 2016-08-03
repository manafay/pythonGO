# List Problem
# def result_matrix(b):
#     for i in range(len(b)):
#         for j in range(len(b[1])):
#             b[i][j] = 0
#     return b


def matrix_addition(a, b):
    c = result(b)

    for i in range(len(a)):
        for j in range(len(a[1])):
          c[i][j] = a[i][j] + b[i][j]
    return c


def result(row,column):
    c = []
    d = []
    for i in range(column):
        c.append(0)

    for j in range(row):
        d.append(c)
    return d

def matrix_multiply(a, b):
    c = result(len(a), len(b[0]))
    for i in range(len(a)):
        for j in range(len(a[1])):
            for k in range(len(b[1])):
                c[i][k] += a[i][j] * b[j][k]
    return c




a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

c = [[1, 1, 1],
     [1, 1, 1],
     [2, 2, 2]]
d = [[2],
     [2],
     [3]]

# print(matrix_addition(a,b))
# print(len(a[1]))
print(matrix_multiply(a, b))