n = ["aad", "daa", "ada", "addda"]
print(any(x == x[::-1] for x in n))
