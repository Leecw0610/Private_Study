
def seqsearch (n, S, x):
    location = 1
    while (location <= n and S[location] != x):
        location += 1
    if (location > n):
        location = 0
    return location

S = [0, 10, 7, 11, 5, 13, 8]
x = 5
location = seqsearch(len(S) - 1, S, x)
print('location =', location)

x = 4
location = seqsearch(len(S) - 1, S, x)
print('location =', location)
