import sys


def n_queens(n):
    def dfs(r, c, rd, ld):
        if r == n:
            return 1

        res = 0
        for j in range(n):
            x = 1 << j
            y = 1 << (r - j + n - 1)
            z = 1 << (r + j)
            if ((x & c) | (y & rd) | (z & ld)) == 0:
                res += dfs(r + 1, c | x, rd | y, ld | z)
        return res

    return dfs(0, 0, 0, 0)


N = int(sys.argv[1])
print(n_queens(N), "ways")
