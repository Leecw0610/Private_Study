def hamiltonian (i, W, vindex):
    n = len(W) - 1
    if (promising(i, W, vindex)):
        if (i == (n - 1)):
            print(vindex[0:n])
        else:
            for j in range(2, n + 1):
                vindex[i + 1] = j
                hamiltonian(i + 1, W, vindex)

def promising (i, W, vindex):
    flag = True
    if ((i == (n - 1)) and not W[vindex[n-1]][vindex[0]]):
        flag = False
    elif ((i > 0) and not W[vindex[i-1]][vindex[i]]):
        flag = False
    else:
        j = 1
        while (j < i and flag):
            if (vindex[i] == vindex[j]):
                flag = False
            j += 1
    return flag
            
n = 4
edges = [
    [1, 2],
    # [1, 3],
    [1, 4], 
    [2, 3],
    [2, 4],
    [3, 4]
]
W = [[False] * (n + 1) for _ in range(n + 1)]
for e in edges:
    W[e[0]][e[1]] = W[e[1]][e[0]] = True
vindex = [-1] * (n + 1)
vindex[0] = 1
hamiltonian(0, W, vindex)
