from typing import List

# class Solution:
#
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         self.r_lset = [set() for i in range(9)]
#         self.c_lset = [set() for i in range(9)]
#         self.m_lset = [set() for i in range(9)]
#
#         for r in range(9):
#             for c in range(9):
#                 v = board[r][c]
#                 if v == ".":
#                     board[r][c] = None
#                     continue
#
#                 v = int(v)
#                 board[r][c] = v
#                 self.r_lset[r].add(v)
#                 self.c_lset[c].add(v)
#                 m = r // 3 * 3 + c // 3
#                 self.m_lset[m].add(v)
#
#         return self.dfs(board)
#
#     def dfs(self, board, offset=None):
#         if offset is None: offset = 0
#
#         for pos in range(offset, 81):
#             r = pos//9
#             c = pos%9
#             m = r//3*3+c//3
#
#             v = board[r][c]
#             if v is not None: continue
#
#             sum_set = set()
#             sum_set |= self.r_lset[r]
#             sum_set |= self.c_lset[c]
#             sum_set |= self.m_lset[m]
#
#             res = False
#             for i in range(1, 10):
#                 if i in sum_set:continue
#
#                 self.r_lset[r].add(i)
#                 self.c_lset[c].add(i)
#                 self.m_lset[m].add(i)
#
#                 res |= self.dfs(board, pos+1)
#                 if res: return True
#
#                 self.r_lset[r].discard(i)
#                 self.c_lset[c].discard(i)
#                 self.m_lset[m].discard(i)
#
#             return res
#         return True


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku(
        [[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
         ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
         ["9", ".", ".", ".", ".", ".", ".", ".", "."]]))


