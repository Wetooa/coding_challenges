from heapq import heappop, heapify, heappush

q = [(4, 2)]
heapify(q)

n: int = int(input("Enter n: "))

for i in range(3, n + 1):
    curr = [heappop(q)]
    while q:
        next = heappop(q)
        if next[0] != curr[-1][0]: 
            heappush(q, next)
            break
        curr.append(next)

    if i < curr[-1][0]:
        heappush(q, (i ** 2, i))
    else:
        curr = [(a + b, b) for a, b in curr]

    while curr: heappush(q, curr.pop())

print(sorted( [b for _, b in q] ))
