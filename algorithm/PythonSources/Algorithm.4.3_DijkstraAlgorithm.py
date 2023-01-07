def dijkstra (W):
    n = len(W) - 1
    F = []
    touch = [-1] * (n + 1)
    length = [-1] * (n + 1)
    for i in range(2, n + 1):
        touch[i] = 1
        length[i] = W[1][i]
    print_tl(F, touch, length)
    for _ in range(n - 1):
        minValue = INF
        for i in range(2, n + 1):
            if (0 <= length[i] and length[i] < minValue):
                minValue = length[i]
                vnear = i
        edge = (touch[vnear], vnear, W[touch[vnear]][vnear])
        F.append(edge)
        for i in range(2, n + 1):
            if (length[i] > length[vnear] + W[vnear][i]):
                length[i] = length[vnear] + W[vnear][i]
                touch[i] = vnear
        length[vnear] = -1
        print_tl(F, touch, length)
    return F

def length (F):
    total = 0
    for e in F:
        total += e[2]
    return total

def print_tl (F, touch, length):
    print('F = ', end = '')
    print(F)
    print('   touch: ', end = '')
    print(touch)
    print('  length: ', end = '')
    print(length)
    
INF = 999
W = [
    [-1, -1, -1, -1, -1, -1],
    [-1, 0, 7, 4, 6, 1],
    [-1, INF, 0, INF, INF, INF],
    [-1, INF, 2, 0, 5, INF],
    [-1, INF, 3, INF, 0, INF],
    [-1, INF, INF, INF, 1, 0],
]

F = dijkstra(W)
for i in range(len(F)):
    print(F[i])

print("Shortest Path Length is", length(F))
