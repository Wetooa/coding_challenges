from typing import List, Optional, Any


class BTree:
    def __init__(self, max_keys: int) -> None:
        self.MAX_KEYS = max_keys
        self.root = None

    class BTreeNode:
        def __init__(
            self,
            keys: List[Any] = [],
            child: List["BTree.BTreeNode"] = [],
            parent: Optional["BTree.BTreeNode"] = None,
        ) -> None:
            self.keys = keys
            self.child = child
            self.parent = parent

        def split(self):
            half = len(self.keys) // 2
            left = BTree.BTreeNode(
                self.keys[:half], self.child[: half + 1], self.parent
            )
            right = BTree.BTreeNode(
                self.keys[half + 1 :], self.child[half + 1 :], self.parent
            )
            return left, right, self.keys[half]

        @property
        def is_leaf(self):
            return len(self.child) == 0

    def __lower_bound_key(self, node: BTreeNode, key):
        for i, node_keys in enumerate(node.keys):
            if key <= node_keys:
                return i
        return len(node.keys)

    def __check_overflow(self, node: BTreeNode):
        if len(node.keys) <= self.MAX_KEYS:
            return

        left, right, middle_key = node.split()

        if node is self.root:
            self.root = BTree.BTreeNode([middle_key], [left, right])
            left.parent = self.root
            right.parent = self.root
        else:
            assert node.parent is not None
            index = self.__lower_bound_key(node.parent, middle_key)
            node.parent.keys.insert(index, middle_key)
            node.parent.child[index] = left
            node.parent.child.insert(index + 1, right)

    def __insert(self, node: Optional[BTreeNode], key):
        if node is None:
            self.root = BTree.BTreeNode([key])
            return

        index = self.__lower_bound_key(node, key)

        if node.is_leaf:
            node.keys.insert(index, key)
        else:
            self.__insert(node.child[index], key)

        self.__check_overflow(node)

    def insert(self, key: object):
        self.__insert(self.root, key)

    # FIX: unfinished
    def __check_underflow(self, node: BTreeNode):
        if len(node.keys) >= self.MAX_KEYS // 2:
            return

        if node is self.root:
            if len(node.keys) >= 1:
                return

            keys = []
            children = []
            for child in node.child:
                keys.extend(child.keys)
                children.extend(child.child)

            self.root = BTree.BTreeNode(keys, children)
            self.__check_overflow(self.root)
            return

        assert node.parent is not None
        index = node.parent.child.index(node)

        if node.is_leaf:
            can_borrow = index < len(node.parent.child) - 1

            if can_borrow:
                sibling = node.parent.child[index + 1]
                node.parent.keys.insert(index, sibling.keys.pop(0))
                node.keys.append(node.parent.keys.pop(index))
            else:
                pass
        else:
            largest_key = node.child[index].keys.pop()
            node.keys.insert(0, largest_key)
            self.__check_underflow(node.child[index])

    # FIX: unfinished
    def __delete(self, node: Optional[BTreeNode], key):
        if node is None:
            return

        index = self.__lower_bound_key(node, key)

        if index < len(node.keys) and node.keys[index] == key:
            node.keys.pop(index)
            self.__check_underflow(node)
        else:
            self.__delete(node.child[index], key)

    # FIX: unfinished
    def delete(self, key):
        self.__delete(self.root, key)

    def __print(self, node: Optional[BTreeNode], depth: int):
        if node is None:
            return

        print("\t" * depth + "Keys: ", node.keys)
        print("\t" * depth + "Depth: ", depth)
        for child in node.child:
            self.__print(child, depth + 1)

    def print(self):
        self.__print(self.root, 0)


btree = BTree(4)

for i in range(1, 20):
    print("Inserting:", i)
    btree.insert(i)
    btree.print()
    print()
