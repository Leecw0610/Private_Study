def bin2 (n, k):
    B = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if (j == 0 or j == i):
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    return B[n][k]

for n in range(10):
    for k in range(n + 1):
        print(bin2(n, k), end = " ")
    print()
    
