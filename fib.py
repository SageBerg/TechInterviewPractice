def iter_fib(n):
    if n == 1 or n == 2:
        return 1
    fibs = [1, 1]
    i = 2
    while len(fibs) < n:
        fibs.append(fibs[i - 1] + fibs[i - 2])
        i += 1
    return fibs[n - 1]

def rec_fib(n):
    if n == 1 or n == 2:
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)

for i in range(1, 20):
    print rec_fib(i), iter_fib(i)

