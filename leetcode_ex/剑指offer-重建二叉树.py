# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return None
        if len(preorder) == 1: return TreeNode(preorder[0])

        pos = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:pos+1], inorder[:pos])
        root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
        return root

if __name__ == '__main__':
    print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))
