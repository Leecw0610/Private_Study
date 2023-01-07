def sum_of_subsets (i, weight, total):
    n = len(w) - 1
    if (promising(i, weight, total)):
        if (weight == W):
            print(include[1: n + 1])
        else:
            include[i + 1] = True
            sum_of_subsets(i + 1, weight + w[i+1], total - w[i+1])
            include[i + 1] = False
            sum_of_subsets(i + 1, weight, total - w[i+1])

def promising (i, weight, total):
    if ((weight + total >= W) and 
        (weight == W or weight + w[i+1] <= W)):
        return True
    else:
        return False

n = 5
W = 21
w = [0, 5, 6, 10, 11, 16]
total = sum(w)
include = [False] * (n + 1)
print(total)
sum_of_subsets(0, 0, total)
