
# Algorithm 1.4: Matrix Muiltiplication 
def matrixmult (A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def madd (A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def msub (A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def divide(A):
    n = len(A)
    m = n // 2
    A11 = [[0] * m for _ in range(m)]
    A12 = [[0] * m for _ in range(m)]
    A21 = [[0] * m for _ in range(m)]
    A22 = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            A11[i][j] = A[i][j]
            A12[i][j] = A[i][j + m]
            A21[i][j] = A[i + m][j]
            A22[i][j] = A[i + m][j + m]
    return A11, A12, A21, A22

def conquer(M1, M2, M3, M4, M5, M6, M7):
    C11 = madd(msub(madd(M1, M4), M5), M7)
    C12 = madd(M3, M5)
    C21 = madd(M2, M4)
    C22 = madd(msub(madd(M1, M3), M2), M6)
    m = len(C11)
    n = 2 * m
    C = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            C[i][j] = C11[i][j]
            C[i][j + m] = C12[i][j]
            C[i + m][j] = C21[i][j]
            C[i + m][j + m] = C22[i][j]
    return C

def strassen (A, B):
    n = len(A)
    if (n <= threshold):
        return matrixmult(A, B)
    A11, A12, A21, A22 = divide(A)
    B11, B12, B21, B22 = divide(B)
    M1 = strassen(madd(A11, A22), madd(B11, B22))
    M2 = strassen(madd(A21, A22), B11)
    M3 = strassen(A11, msub(B12, B22))
    M4 = strassen(A22, msub(B21, B11))
    M5 = strassen(madd(A11, A12), B22)
    M6 = strassen(msub(A21, A11), madd(B11, B12))
    M7 = strassen(msub(A12, A22), madd(B21, B22))
    return conquer(M1, M2, M3, M4, M5, M6, M7)

threshold = 2
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7],
]

B = [
    [8, 9, 1, 2],
    [3, 4, 5, 6],
    [7, 8, 9, 1],
    [2, 3, 4, 5],
]

print('threshold =', threshold)
print('A =', A)
print('B =', B)
C = strassen(A, B)
for i in range(len(C)):
    print('C[%d] = '%(i), C[i])

D = matrixmult(A, B)    
for i in range(len(D)):
    print('D[%d] = '%(i), D[i])
