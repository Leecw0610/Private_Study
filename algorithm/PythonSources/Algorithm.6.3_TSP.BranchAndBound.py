from queue import PriorityQueue

class SSTNode:
    
    def __init__ (self, level):
        self.level = level
        self.path = []
        self.bound = 0

    def contains(self, x):
        for i in range(len(self.path)):
            if (self.path[i] == x):
                return True
        return False    

def hasOutgoing(v, path):
    for i in range(0, len(path) - 1):
        if (path[i] == v):
            return True
    return False

def hasIncoming(v, path):
    for i in range(1, len(path)):
        if (path[i] == v):
            return True
    return False

def length(path, W):
    total = 0
    prev = 1
    for i in range(len(path)):
        if (i != 0):
            prev = path[i - 1]
        total += W[prev][path[i]] 
        prev = path[i]
    return total


def bound(v, W):
    n = len(W) - 1
    total = length(v.path, W)
    for i in range(1, n + 1):
        if (hasOutgoing(i, v.path)):
            continue
        min = INF
        for j in range(1, n + 1):
            if (i == j):
                continue
            if (hasIncoming(j, v.path)):
                continue
            if (j == 1 and i == v.path[len(v.path) - 1]):
                continue
            if (min > W[i][j]):
                min = W[i][j]
        total += min
    return total

def travel2 (W):
    global minlength, opttour
    n = len(W) - 1
    PQ = PriorityQueue()
    v = SSTNode(0)
    v.path = [1]
    v.bound = bound(v, W)
    minlength = INF
    PQ.put((v.bound, v))
    while (not PQ.empty()):
        v = PQ.get()[1]
        if (v.bound < minlength):
            for i in range(2, n + 1):
                if (v.contains(i)): 
                    continue
                u = SSTNode(v.level + 1)
                u.path = v.path[:]
                u.path.append(i)
                if (u.level == n - 2):
                    for k in range(2, n + 1):
                        if (not u.contains(k)):
                            u.path.append(k)
                    u.path.append(1)
                    if (length(u.path, W) < minlength):
                        minlength = length(u.path, W)
                        opttour = u.path[:]
                else:
                    u.bound = bound(u, W)
                    if (u.bound < minlength):
                        PQ.put((u.bound, u))
      
INF = 999
W = [
    [-1, -1, -1, -1, -1, -1],
    [-1, 0, 14, 4, 10, 20],
    [-1, 14, 0, 7, 8, 7],
    [-1, 4, 5, 0, 7, 16],
    [-1, 11, 7, 9, 0, 2],
    [-1, 18, 7, 17, 4, 0],
]

minlength = INF
opttour = None
travel2(W)

print("minlength =", minlength)
print("optimal tour =", opttour)
