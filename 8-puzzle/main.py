import numpy as np
from collections import deque


DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = 2


# NOTE: TO BE DONE: Add Heuristics Function
def heuristic():
    # NOTE: Number of Misplaced Tiles
    # NOTE: Total Manhattan Distance
    pass


def find_empty(state):
    for i in range(N):
        for j in range(N):
            if state[i][j] == 0:
                return (i, j)
    raise Exception("No empty cell found")


def find_actions(state):
    r, c = find_empty(state)
    actions = []

    for dr, dc in DIR:
        x, y = r + dr, c + dc
        if 0 <= x < N and 0 <= y < N:
            actions.append((x, y, r, c))
    return actions


def do_action(state, actions):
    x, y, r, c = actions
    new_state = np.copy(state)
    new_state[r][c], new_state[x][y] = new_state[x][y], new_state[r][c]
    return new_state


def is_goal(state):
    for i in range(N):
        for j in range(N):
            if i == N - 1 and j == N - 1:
                return True
            if state[i][j] != i * N + j + 1:
                return False
    return True


def hash_state(state):
    return hash(str(state.reshape(-1)))


def is_visited(state):
    return hash_state(state) in visited


def add_visited(state):
    visited.add(hash_state(state))


def solve(start_state):
    q = deque([start_state])
    add_visited(start_state)

    while q:
        state = q.popleft()

        if is_goal(state):
            return True

        actions = find_actions(state)

        for action in actions:
            new_state = do_action(state, action)
            if not is_visited(new_state):
                add_visited(new_state)
                q.append(new_state)
        return False


count = 0

for _ in range(10000):
    start = np.arange(N * N)
    np.random.shuffle(start)
    start = start.reshape(N, N)
    visited = set()

    if solve(start):
        count += 1
        print(start)
print(count)
