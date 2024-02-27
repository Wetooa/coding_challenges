from math import sqrt

# n = int(input("Until what number: "))
n = 50000
d = [True] * (n + 1)

for i in range(2, int(sqrt(n)) + 1):
    if not d[i]:
        break
    for j in range(i * 2, n + 1, i):
        d[j] = False


primes = [i for i in range(2, n + 1) if d[i]]

print(primes)
print(len(primes))
