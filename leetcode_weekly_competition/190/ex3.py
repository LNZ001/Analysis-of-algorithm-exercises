import math
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def check(self, root, pos=None):
        if pos is None:
            pos = 0
        if root is None:
            return True
        v = root.val
        if v is None:
            return True
        else:
            # ######### 进行0-1置换 ###########
            if self.queue_list[v-1] == 1:
                self.queue_list[v-1] = 0
            else:
                self.queue_list[v-1] = 1

            res1 = self.check(root.left)

            res2 = self.check(root.right)
            if res1 and res2:
                self.checking()

            # ######### 结束当前分支后消除0-1置换 ###########
            if self.queue_list[v-1] == 1:
                self.queue_list[v-1] = 0
            else:
                self.queue_list[v-1] = 1

            return False


    def checking(self):
        if self.queue_list.count(1) <= 1:
            self.count += 1

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.queue_list = [0]*9
        self.check(root)
        return self.count


if __name__ == '__main__':
    tuple_list = [
        ([2,3,1,3,1,None,1],),
        ([2,1,1,1,3,None, None, None, None, None,1],),
        ([9],)
    ]
    for t in tuple_list:
        print(Solution().pseudoPalindromicPaths(*t))