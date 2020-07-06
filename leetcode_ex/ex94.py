# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        results = []
        stacks = []
        while root or len(stacks) != 0:
            while root:
                stacks.append(root)
                root = root.left

            k = stacks.pop()
            results.append(k.val)
            if root.right is not None:
                root = k.right

        return results

if __name__ == '__main__':
    print(Solution().inorderTraversal())