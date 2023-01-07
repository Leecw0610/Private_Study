def location (S, low, high):
    if (low > high):
        return 0
    else:
        mid = (low + high) // 2
        print(low, mid, high)
        if (x == S[mid]):
            return mid
        elif (x < S[mid]):
            return location(S, low, mid - 1)
        else:
            return location(S, mid + 1, high)
    
S = [-1, 10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45, 47]
x = 18
loc = location(S, 1, len(S) - 1)
print('S =', S)
print('x =', x)
print('loc = ', loc)
