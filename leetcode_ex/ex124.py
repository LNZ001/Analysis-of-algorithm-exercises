# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_value = []
        self.max_value = float('-inf')

        def dfs(head) -> (int, int):
            if head is None:
                return 0, 0

            # ########## 似乎没有好的办法保证至少有一个,因为max中可能取子节点不要的情况最好, 所以不能够要求最底层至少有一个节点. ##########
            # ########## 解决办法: 如果结果是0, 就用最大单值替代 ##########
            self.max_value = max(self.max_value, head.val)

            canFoldLeft, unFoldLeft = dfs(head.left)
            canFoldRight, unFoldRight = dfs(head.right)

            can = max(canFoldLeft, canFoldRight, max(0, unFoldLeft) + max(0, unFoldRight) + head.val)
            un = max(0, unFoldRight, unFoldLeft) + head.val
            return can, un

        canFold, unFold = dfs(root)
        if canFold == 0:
            return self.max_value
        return canFold


if __name__ == '__main__':
    print(Solution().maxPathSum(TreeNode(-3)))