"""
https://en.wikipedia.org/wiki/Fenwick_tree


FernWick Tree

> A complicated ass tree that requires big ass brain

Few key points
- Tree is 1-indexed
- Tree right is inclusive on the right
"""


class FernWick:

    def __init__(self, n) -> None:
        self.n = n
        self.d = [0] * (self.n + 1)

    """
    FernWick Update:

    - The idea here is to update the elements that contain the index 'i'
    - ALSO! The idea of update is to ADD delta to the current value

    1. We start at index 'i' and add the value 'x' to it.
    2. We move to the next index which contains 'i' (this is done by adding the lowbit (lowest flipped bit) of 'i' to 'i').
    3. We keep doing this while 'i' is less than or equal to the size of the array.
    """

    def update(self, i, x):
        while i <= self.n:
            self.d[i] += x
            i += i & -i

    """
    FernWick Sum:

    - The idea here is recursively move up to the parent while getting the sum
    - This makes sense if you have an image

    1. We start at index 'i' and add its value to 'res'
    2. We move up to the parent by removing the lowbit 
    3. We keep doing this while 'i' is greater than 0
    """

    def get(self, i):
        res = 0
        while i > 0:
            res += self.d[i]
            i -= i & -i
        return res


n = 16
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

T = FernWick(n)

for i in range(len(array)):
    T.update(i + 1, array[i])

print(T.get(4))  # sum of 1, 2, 3, 4

T.update(2, 10)

print(T.get(1))  # sum of 1
print(T.get(2))  # sum of 1, 12
print(T.get(3))
print(T.get(4))
