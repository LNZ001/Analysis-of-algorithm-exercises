from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        stack = []
        while True:
            while root:
                # ########## 如果右子树不为空, 就先添加右子数, 再添加根. ##########
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            if (root.right is not None) and len(stack) > 0 and (stack[-1] == root.right):
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                res.append(root.val)
                root = None

            if len(stack) <= 0:
                break
        return res


# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         queue = []
#         cur = root
#         result = []
#         while cur or queue:
#             while cur:
#                 # 前序遍历
#                 result.append(cur.val)
#                 queue.append(cur)
#                 cur = cur.right
#
#             cur = queue.pop()
#             # 中序遍历
#             # result.append(cur.val)
#             cur = cur.left
#
#         result.reverse()
#         return result

if __name__ == '__main__':
    from tools.analysis import analysis_tree
    print(Solution().postorderTraversal(analysis_tree([1, None, 2, None, None, 3])))