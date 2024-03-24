t = int(input().strip())
for _ in range(t):
    n = input().strip()
    count = 0
    for x in range(len(n)):
        if n[x] != "0" and int(n) % int(n[x]) == 0:
            count += 1
    print(count)  