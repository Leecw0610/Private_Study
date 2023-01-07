
def partition (S, low, high):
    pivotitem = S[low]
    j = low
    for i in range(low + 1, high + 1):
        print(i, j, S)
        if (S[i] < pivotitem):
            j += 1
            S[i], S[j] = S[j], S[i] # swap
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low] # swap
    return pivotpoint

def quicksort (S, low, high):
    if (high > low):
        pivotpoint = partition(S, low, high)
        # print(S)
        quicksort(S, low, pivotpoint - 1)
        quicksort(S, pivotpoint + 1, high)

# S = [15, 22, 13, 27, 12, 10, 20, 25]
# print('Before:', S)
# quicksort(S, 0, len(S) - 1)
# print(' After:', S)

# S = [15, 22, 13, 27, 12, 10, 20, 25]
# print('Before:', S)
# partition(S, 0, len(S) - 1)
# print(' After:', S)

def partition2 (S, low, high):
    pivotitem = S[low]
    i = low + 1
    j = high
    while (i <= j):
        while (S[i] < pivotitem):
            i += 1
        while (S[j] > pivotitem):
            j -= 1
        if (i < j):
            S[i], S[j] = S[j], S[i] # swap
        print(i, j, S)
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low] # swap
    return pivotpoint

def quicksort2 (S, low, high):
    if (high > low):
        pivotpoint = partition2(S, low, high)
        # print(S)
        quicksort2(S, low, pivotpoint - 1)
        quicksort2(S, pivotpoint + 1, high)

# S = [15, 22, 13, 27, 12, 10, 20, 25]
S = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]

print('Before:', S)
quicksort2(S, 0, len(S) - 1)
print(' After:', S)

# S = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
# print('Before:', S)
# partition2(S, 0, len(S) - 1)
# print(' After:', S)
