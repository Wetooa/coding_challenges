n = 8
edges = [[1], [2], [0], [4, 7], [5], [0, 6], [0, 2, 4], [3, 5]]


# FIX: UNFINISHED CODE HERE T_T

low_link = [i for i in range(n)]
visited = set()
stack_set = set()
ed = [set(i) for i in edges]


def solve(node):
    stack = []
    stack_set = set()

    while stack:
        top = stack[-1]

        for nex in ed[top]:
            if nex not in visited:
                visited.add(nex)
                stack.append(nex)
                ed.remove(nex)
                continue

        if len(ed[top]) == 0:
            mini = top
            for nex in edges[top]:
                if nex in stack_set:
                    mini = min(mini, top)

            while stack and mini in stack_set:
                low_link[stack[-1]] = mini
                stack_set.remove(stack.pop())


for i in range(n):
    solve(i)

print(low_link)
