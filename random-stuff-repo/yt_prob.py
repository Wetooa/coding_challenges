a = [1, 3, 4, 1, 4, 6, 2]
b = 3
c = {}

for x in range(len(a)):
    for y in range(x+1, len(a)):
        if a[x] + a[y] == b:
            print(str(a[x]) + " " + str(a[y]))


a = set(a)
for x in a:
    if b - x in a:
        print(str(x) + " " + str(b - x))