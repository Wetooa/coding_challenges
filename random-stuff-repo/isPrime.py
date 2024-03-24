def isPrime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


q = 100
for j in range(1, q):
    print(j, isPrime(j))
