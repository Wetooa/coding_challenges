import numpy as np

N = 14
M = 10
grid = [[i * M + j + 1 for j in range(M)] for i in range(N)]
blocked = set(
    [
        4,
        5,
        6,
        13,
        17,
        18,
        21,
        25,
        28,
        36,
        38,
        42,
        44,
        46,
        48,
        54,
        56,
        59,
        61,
        68,
        69,
        74,
        84,
        85,
        88,
        105,
        107,
        115,
    ]
)


print(np.matrix(grid))


def convert(n):
    n -= 1
    return (n // M, n % M)


def rev_convert(x, y):
    return x * M + y + 1


START = 24
END = 87

convert_start = convert(START)
convert_end = convert(END)

q = [convert_start]
fringe = [(2, 3, 2, 3)]
visited = set([convert_start])

DIR = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while q:
    x, y = q.pop()

    if (x, y) == convert_end:
        break

    for dr, dc in DIR:
        r = x + dr
        c = y + dc
        if (
            r >= 0
            and c >= 0
            and r < N
            and c < M
            and (r, c) not in visited
            and rev_convert(r, c) not in blocked
        ):
            visited.add((r, c))
            q.append((r, c))
            fringe.append((r, c, x, y))

print(fringe)

for x, y, ox, oy in fringe:
    print(rev_convert(x, y), rev_convert(ox, oy))


d = {rev_convert(x, y): rev_convert(ox, oy) for x, y, ox, oy in fringe}

path = []
curr = END

while d[curr] != curr:
    path.append(curr)
    curr = d[curr]

path = [START] + path[::-1]
print("Path:", path)
