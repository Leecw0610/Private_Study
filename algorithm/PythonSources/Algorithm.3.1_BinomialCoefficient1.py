def bin (n, k):
    if (k == 0 or n == k):
        return 1
    else:
        return bin(n - 1, k - 1) + bin(n - 1, k)

for n in range(10):
    for k in range(n + 1):
        print(bin(n, k), end = " ")
    print()
