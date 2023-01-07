def matrixmult (A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
print('A =', A)
print('B =', B)
C = matrixmult(A, B)
print('C =', C)
