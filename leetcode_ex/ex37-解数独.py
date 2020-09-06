from typing import List

class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.r_lset = [set() for i in range(9)]
        self.c_lset = [set() for i in range(9)]
        self.m_lset = [set() for i in range(9)]
        self.board = board

        for r in range(9):
            for c in range(9):
                v = self.board[r][c]
                if v == ".":
                    continue

                self.r_lset[r].add(v)
                self.c_lset[c].add(v)
                m = r // 3 * 3 + c // 3
                self.m_lset[m].add(v)

        return self.dfs(self.board)


    def dfs(self, board, offset=None):
        if offset is None: offset = 0

        for pos in range(offset, 81):
            r = pos//9
            c = pos%9
            m = r//3*3+c//3

            v = board[r][c]
            if v != ".": continue

            sum_set = set()
            sum_set |= self.r_lset[r]
            sum_set |= self.c_lset[c]
            sum_set |= self.m_lset[m]

            res = False
            for i in range(1, 10):
                if str(i) in sum_set:continue
                board[r][c] = str(i)
                self.r_lset[r].add(str(i))
                self.c_lset[c].add(str(i))
                self.m_lset[m].add(str(i))


                res |= self.dfs(board, pos+1)
                if res: return True

                board[r][c] = "."
                self.r_lset[r].discard(str(i))
                self.c_lset[c].discard(str(i))
                self.m_lset[m].discard(str(i))

            return res
        return True

if __name__ == '__main__':
    print(Solution().solveSudoku())