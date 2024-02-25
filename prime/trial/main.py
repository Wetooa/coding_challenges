n = 10000
primes = []

for i in range(2, n + 1):
    if not any([i % p == 0 for p in primes]):
        primes.append(i)

print(primes)
