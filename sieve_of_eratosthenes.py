def sieve(n):
    primes = []
    composites = set()
    for i in range(2, n):
        if i not in composites:
            primes.append(i)
            for j in range(i * 2, n, i):
                composites.add(j)
    return primes
        
def main():
    primes = sieve(1000)
    print primes[:100]

main()
