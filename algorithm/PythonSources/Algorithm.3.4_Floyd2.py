def floyd2 (W):
    n = len(W)
    D = W
    P = [[-1] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (D[i][j] > D[i][k] + D[k][j]):
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k
    return D, P

def path (P, u, v):
    if (P[u][v] != -1):
        path(P, u, P[u][v])
        print('v%d'%(P[u][v]), end='-> ')
        path(P, P[u][v], v)

INF = 999
W = [
    [0, 1, INF, 1, 5],
    [9, 0, 3, 2, INF],
    [INF, INF, 0, 4, INF],
    [INF, INF, 2, 0, 3],
    [3, INF, INF, INF, 0]
]

D, P = floyd2(W)
for i in range(len(D)):
    print(D[i])
for i in range(len(P)):
    print(P[i])

u = 0
v = 2
print('shortest path from v%d to v%d:'%(u, v), end=' ')
print('v%d'%(u), end='-> ')
path(P, u, v)
print('v%d'%(v), end=' ')