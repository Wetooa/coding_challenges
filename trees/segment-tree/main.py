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
                return Node(arr[l], l, r)
            if l > r:
                return None

            mid = (l + r) // 2
            x = create(l, mid)
            y = create(mid + 1, r)

            return Node(
                self.func(x.data if x else default, y.data if y else default),
                l,
                r,
                x,
                y,
            )

        self.root = create(0, len(arr) - 1)

    def find(self, l, r):

        def get(tree):
            if not tree:
                return self.default

            x, y = tree.left_index, tree.right_index
            if l <= x <= y <= r:
                return tree.data

            left = get(tree.left)
            right = get(tree.right)
            return self.func(left, right)

        return get(self.root)

    def update(self, index, value):

        def adjust(tree):
            if not tree:
                return
            x, y = tree.left_index, tree.right_index
            if x == y:
                if index == x:
                    tree.data = value
                return tree

            left = adjust(tree.left)
            right = adjust(tree.right)
            tree.data = self.func(
                left.data if left else self.default,
                right.data if right else self.default,
            )
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


arr = [1, 2, 3, 5, 3, 6, 7, 8, 3, 2, 1, 3, 5, 6, 3, 5]
func = min

T = SegmentTree(arr, func, int(1e9))


x = 6
y = 10

print(T.find(x, y))
print(min(arr[x : y + 1]))

arr[5] = 0
T.update(5, 0)

print(T.find(x, y))
print(min(arr[x : y + 1]))
