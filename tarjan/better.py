def find_scc(edges):

    n = max(max(t) for t in edges) + 1
    connected_edges = [[] for _ in range(n)]
    time_visited = {}
    visited = set([0])
    scc = []

    for a, b in edges:
        connected_edges[a].append(b)
        connected_edges[b].append(a)

    def dfs(curr, parent, timestamp):

        time_visited[curr] = timestamp

        for nex in connected_edges[curr]:
            if nex == parent:
                continue

            if nex not in visited:
                visited.add(nex)
                dfs(nex, curr, timestamp + 1)

            if time_visited[nex] > timestamp:
                scc.append(nex)

            time_visited[curr] = min(time_visited[curr], time_visited[nex])

    dfs(0, -1, 1)

    print(scc)


edges = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (5, 3), (0, 5)]
"""
0 -- 1 -- 2
|    |
|    3
|  / | 
5 -- 4
"""


edges = [(0, 1), (1, 2), (2, 4), (3, 4), (4, 5), (0, 5)]
"""
0 -- 1 -- 2
 \\      /
  5 -- 4 -- 3
"""


find_scc(edges)
