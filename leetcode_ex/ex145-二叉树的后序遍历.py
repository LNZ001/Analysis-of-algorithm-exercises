# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:

# ######### 先序、中序 ###########
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return None
        if len(preorder) == 1: return TreeNode(preorder[0])

        pos = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:pos+1], inorder[:pos])
        root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
        return root

    result = []

    '''
    递归法：区别只是self.result.append的位置。
    '''
    def iterorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None : return self.result
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.result

    '''
    迭代法
    '''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return self.result
        queue = []
        cur = root
        while cur is not None or len(queue) != 0:
            while cur is not None:
                '''先序记录的位置.'''
                print(cur.val)
                queue.append(cur)
                cur = cur.left

            cur = queue.pop()
            '''
            中序的位置
            '''
            self.result.append(cur.val)
            cur = cur.right

        return self.result

    def postorderTraversal(self, root):
        if root is None: return self.result
        queue = []
        cur = root
        while cur is not None or len(queue) != 0:
            while cur is not None:
                '''先序记录的位置.'''
                # print(cur.val)
                queue.append(cur)
                if cur.left:
                    cur = cur.left
                else:
                    cur = cur.right

            cur = queue.pop()
            self.result.append(cur.val)
            if queue and cur == queue[-1].left:
                cur = queue[-1].right
            else:
                cur = None

        return self.result


if __name__ == '__main__':
    s = Solution()
    tree = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(Solution().postorderTraversal(tree))
