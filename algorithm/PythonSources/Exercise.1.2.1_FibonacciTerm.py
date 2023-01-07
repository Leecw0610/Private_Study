def fib3 (n):
    if (n <= 1):
        return n
    else:
        pprv = 0
        prv = 1
        for i in range(2, n + 1):
            nxt = pprv + prv
            pprv, prv = prv, nxt
        return prv

for i in range(11):
    print(fib3(i), end=" ")