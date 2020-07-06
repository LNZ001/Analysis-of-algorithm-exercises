# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
import itertools

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # ########## 首先计算全排列 ##########
        queue = list(itertools.permutations(range(1, n+1)))

        print(queue)

        results = []
        for elements in queue:
            root = TreeNode(elements[0])
            for i in range(1, len(elements)):
                self.insert(root, elements[i])
            results.append(root)

        return results

    def insert(self, root, n):

        if n < root.val:
            if root.left is None:
                root.left = TreeNode(n)
                return
            self.insert(root.left, n)
        elif n > root.val:
            if root.right is None:
                root.right = TreeNode(n)
                return
            self.insert(root.right, n)



if __name__ == '__main__':
    print(Solution().generateTrees(3))