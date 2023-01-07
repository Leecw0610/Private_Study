def minimum (M, d, i, j):
    minValue = INF
    minK = 0
    for k in range(i, j):
        value = M[i][k] + M[k + 1][j]
        value += d[i - 1] * d[k] * d[j]
        if (minValue > value):
            minValue = value
            minK = k
    return minValue, minK

def minmult (d):
    n = len(d) - 1
    M = [[-1] * (n + 1) for _ in range(n + 1)]
    P = [[-1] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        M[i][i] = 0
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i][j], P[i][j] = minimum(M, d, i, j)
    return M, P

def order (P, i, j):
    if (i == j):
        print('A%d'%(i), end='')
    else:
        k = P[i][j]
        print('(', end = '')
        order(P, i, k)
        order(P, k + 1, j)
        print(')', end = '')

INF = 999
d = [5, 2, 12, 15, 6, 7, 8]
M, P = minmult(d)
print('M = ')
for i in range(1, len(M)):
    print(M[i][1:])
print('P = ')
for i in range(1, len(P)):
    print(P[i][1:])

print('minimum order: ', end = '')
order(P, 1, len(d) - 1)


