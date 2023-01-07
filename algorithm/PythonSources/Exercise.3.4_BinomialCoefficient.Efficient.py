def bin3 (n, k):
    if (k > n // 2):
        k = n - k
    B = [0] * (k + 1)
    B[0] = 1
    for i in range(1, n + 1):
        j = min(i, k)
        while (j > 0):
            B[j] = B[j] + B[j - 1]
            j -= 1
        for n in range(min(i, k) + 1):
            print(B[n], end=" ")
        print()
    return B[k]

for n in range(10):
    for k in range(n + 1):
        print(bin3(n, k), end=" ")
    print()

print(bin3(9, 8))