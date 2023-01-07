def feasible (K, deadline):
    for i in range(1, len(K) + 1):
        if (i > deadline[K[i - 1]]):
            return False
    return True    

deadline = [0, 3, 1, 1, 3, 1, 3, 2]
# K = [2, 7, 1, 4]
# print(K, feasible(K, deadline))

def insert(J, i, deadline):
    K = J[:]
    for j in range(len(J), 0, -1):
        if (deadline[i] >= deadline[K[j-1]]):
            j += 1
            break
    K.insert(j - 1, i)
    return K

deadline = [0, 3, 1, 1, 3, 1, 3, 2]
J = [2, 1, 4]
K = insert(J, 7, deadline)
print(K)
    
def schedule (deadline):
    n = len(deadline) - 1
    J = [1]
    for i in range(2, n + 1):
        K = insert(J, i, deadline)
        print("K=", K, end=" ")
        if (feasible(K, deadline)):
            print("feasible")
            J = K[:]
        else:
            print("not feasible")
        print("\tJ=", J)
    return J

deadline = [0, 3, 1, 1, 3, 1, 3, 2]
profit = [0, 40, 35, 30, 25, 20, 15, 10]
J = schedule (deadline)
print("Schedule:", J)

maxprofit = 0
for job in J:
    maxprofit += profit[job]
print("Max Profit =", maxprofit)
