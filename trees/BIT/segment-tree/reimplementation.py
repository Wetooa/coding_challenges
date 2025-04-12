class Node:
    def __init__(self, value, left=None, right=None, lIndex=None, rIndex=None):
        self.value = value
        self.left = left
        self.right = right
        self.lIndex = lIndex
        self.rIndex = rIndex


class SegmentTree:

    def __init__(self, arr):

        def build(l, r):
            if l == r:
                return Node(arr[l], None, None, l, r)
            if l > r:
                return Node(0, None, None, -1, -1)

            mid = (l + r) // 2
            x = build(l, mid)
            y = build(mid + 1, r)
            return Node(x.value + y.value, x, y, l, r)

        self.root = build(0, len(arr) - 1)

    def update(self, index, value):

        def traverse(curr):
            if curr.lIndex == curr.rIndex:
                curr.value = value
                return

            l, r = curr.lIndex, curr.rIndex

            if l <= index < r:
                traverse(curr.left)
            else:
                traverse(curr.right)

            curr.value = curr.left.value + curr.right.value

        traverse(self.root)

    def query(self, l, r):

        def traverse(curr, index):
            if not curr:
                return 0

            if curr.lIndex == curr.rIndex:
                return curr.value

            return (
                traverse(curr.left, index)
                if curr.lIndex <= index < curr.rIndex
                else traverse(curr.right, index)
            )

        return (
            traverse(self.root, r) - traverse(self.root, l - 1)
            if l > 0
            else traverse(self.root, r)
        )

    def print(self):
        def traverse(curr):
            if not curr or curr.lIndex == -1:
                return
            print(f"Node: {curr.value}, Range: ({curr.lIndex}, {curr.rIndex})")
            traverse(curr.left)
            traverse(curr.right)

        traverse(self.root)


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6]
    T = SegmentTree(arr)

    T.print()

    print("Initial Segment Tree Sum:", T.query(5))
