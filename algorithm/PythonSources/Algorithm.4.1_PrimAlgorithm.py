def prim (W):
    n = len(W) - 1
    F = []
    nearest = [-1] * (n + 1)
    distance = [-1] * (n + 1)
    for i in range(2, n + 1):
        nearest[i] = 1
        distance[i] = W[1][i]
    print_nd(F, nearest, distance)
    for _ in range(n - 1):
        minValue = INF
        for i in range(2, n + 1):
            if (0 <= distance[i] and distance[i] < minValue):
                minValue = distance[i]
                vnear = i
        edge = (nearest[vnear], vnear, W[nearest[vnear]][vnear])
        F.append(edge) # add edge to F
        distance[vnear] = -1
        for i in range(2, n + 1):
            if (distance[i] > W[i][vnear]):
                distance[i] = W[i][vnear]
                nearest[i] = vnear
        print_nd(F, nearest, distance)
    return F

def cost (F, W):
    total = 0
    for e in F:
        total += W[e[0]][e[1]]
    return total

def print_nd (F, nearest, distance):
    print('F = ', end = '')
    print(F)
    print('   nearest: ', end = '')
    print(nearest)
    print('  distance: ', end = '')
    print(distance)

INF = 999
W = [
    [-1, -1, -1, -1, -1],
    [-1, 0, 1, 3, INF, INF],
    [-1, 1, 0, 3, 6, INF],
    [-1, 3, 3, 0, 4, 2],
    [-1, INF, 6, 4, 0, 5],
    [-1, INF, INF, 2, 5, 0],
]

F = prim(W)
for i in range(len(F)):
    print(F[i])

print("Minimum Cost is ", cost(F, W))


