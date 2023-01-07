def exchange (n, S):
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (S[j] < S[i]):
                S[i], S[j] = S[j], S[i]
        print(S)

S = [-1, 10, 7, 11, 5, 13, 8]
print('Before =', S)
exchange(len(S) - 1, S)
print(' After =', S)
