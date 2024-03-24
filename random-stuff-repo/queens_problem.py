class Solution:
    def solveQueens(self, n: int) -> List(List[str]):
        col = set()
        posDiag = set()
        negDiag - set()

        res = []
        board = [["."]]