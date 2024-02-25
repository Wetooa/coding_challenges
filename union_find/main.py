from collections import deque


class UnionFindGraph:

    def __init__(self, connections: list[list[int]], n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

        edges = [[] for _ in range(n)]
        for a, b in connections:
            edges[a].append(b)
            edges[b].append(a)

        for rep in range(n - 1, -1, -1):
            g_size = 1

            if self.parent[rep] != rep:
                continue

            q = deque([rep])
            while q:
                curr = q.pop()
                for nex in edges[curr]:
                    if rep != nex and self.parent[nex] == nex:
                        g_size += 1
                        self.parent[nex] = rep
                        q.appendleft(nex)

            self.size[rep] = g_size

    def are_connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        else:
            # path compression
            # (make it so that nodes have a 1 depth distance to their representative)
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, a: int, b: int) -> None:
        # if a's graph is larger than b's, swap them!
        # a must connect to b
        if self.size[self.find(a)] > self.size[self.find(b)]:
            a, b = b, a

        self.parent[self.find(a)] = self.find(b)


n = 6
connections = [[0, 1], [2, 0], [5, 4], [4, 3]]
g = UnionFindGraph(connections=connections, n=n)


print(g.are_connected(0, 2))
print(g.are_connected(0, 3))
print(g.are_connected(1, 2))
print(g.are_connected(4, 2))
