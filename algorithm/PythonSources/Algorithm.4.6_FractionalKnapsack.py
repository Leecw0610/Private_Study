def knapsack1(W, w, p):
    n = len(w) - 1
    K = [0] * (n + 1)
    weight = 0
    for i in range(1, n + 1):
        weight += w[i]
        K[i] = w[i]
        if (weight > W):
            K[i] -= (weight - W)
            break;
    return K

w = [0, 2, 5, 8, 7, 40, 13, 24]
p = [0, 15, 12, 8, 8, 7, 5, 2]
W = 30
K = knapsack1(W, w, p)
print(K, sum(K))
price = 0
for i in range(1, len(K)):
    price += p[i] * K[i]
print("Total price is", price)

