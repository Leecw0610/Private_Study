class DisjointSet:

    def __init__ (self, n):
        self.U = []
        for i in range(n):
            self.U.append(i)
    
    def find (self, i):
        j = i
        while (self.U[j] != j):
            j = self.U[j]
        return j

    def union (self, p, q):
        if (p < q):
            self.U[q] = p
        else:
            self.U[p] = q

    def equal (self, p, q):
        if (p == q):
            return True
        else:
            return False

def kruskal (n, E):
    F = []
    dset = DisjointSet(n)
    while (len(F) < n - 1):
        edge = E.pop(0)
        i, j = edge[0], edge[1]
        p = dset.find(i)
        q = dset.find(j)
        if (not dset.equal(p, q)):
            dset.union(p, q)
            F.append(edge)
            print("accepted ", edge)
            print(dset.U)
        else:
            print("discarded", edge)
    return F

def cost (F):
    total = 0
    for e in F:
        total += e[2]
    return total

INF = 999
n = 5
E = [
    [0, 1, 1],
    [2, 4, 2],
    [0, 2, 3],
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [1, 3, 6],
]

F = kruskal(n, E)
for i in range(len(F)):
    print(F[i])

print("Minimum cost is", cost(F))

