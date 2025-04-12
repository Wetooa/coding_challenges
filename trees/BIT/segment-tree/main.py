import random


class Node:
    def __init__(self, data, left_index, right_index, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.left_index = left_index
        self.right_index = right_index


class SegmentTree:

    def __init__(self, arr, func, default) -> None:
        self.func = func
        self.default = default

        def create(l, r):
            if l == r:
                return Node(arr[l], l, r, Node(default, 1, 0), Node(default, 1, 0))
            if l > r:
                return Node(default, l, r)

            mid = (l + r) // 2
            x = create(l, mid)
            y = create(mid + 1, r)

            return Node(self.func(x.data, y.data), l, r, x, y)

        self.root = create(0, len(arr) - 1)

    def find(self, l, r):

        def get(root):
            x, y = root.left_index, root.right_index

            if x > y:
                return self.default
            if l <= x <= y <= r:
                return root.data

            mid = (x + y) // 2
            left = right = self.default

            # NOTE: WHAT A GREAT FOOL YOU ARE ADRIAN
            if max(l, x) <= min(r, mid):
                left = get(root.left)
            if max(l, mid + 1) <= min(r, y):
                right = get(root.right)

            return self.func(left, right)

        return get(self.root)

    def update(self, index, value):

        def adjust(tree):
            x, y = tree.left_index, tree.right_index
            if x == y:
                if index == x:
                    tree.data = value
                return tree

            mid = (x + y) // 2
            if index <= mid:
                adjust(tree.left)
            else:
                adjust(tree.right)

            tree.data = self.func(tree.left.data, tree.right.data)
            return tree

        return adjust(self.root)

    def display(self):

        def print_tree(root, depth):
            if not root:
                return

            print("---" * depth, root.data)
            print_tree(root.left, depth + 1)
            print_tree(root.right, depth + 1)

        print_tree(self.root, 0)


arr = [random.randint(0, 1000) for _ in range(100)]
func = lambda x, y: x + y

T = SegmentTree(arr, func, 0)


x = 6
y = 10

print(T.find(x, y))
print(sum(arr[x : y + 1]))

arr[5] = 0
T.update(5, 0)

print(T.find(x, y))
print(sum(arr[x : y + 1]))


for i in range(len(arr)):
    for j in range(i, len(arr)):
        assert sum(arr[i : j + 1]) == T.find(i, j)
