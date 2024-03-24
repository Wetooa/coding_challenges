t = int(input().strip())
last = 3
while t > last:
    t -= last
    last *= 2
print(last - t + 1) 