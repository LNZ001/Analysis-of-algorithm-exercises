from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        queue = []
        cur = root
        result = []
        while cur or queue:
            while cur:
                # 前序遍历
                result.append(cur.val)
                queue.append(cur)
                cur = cur.left


            cur = queue.pop()
            # 中序遍历
            # result.append(cur.val)
            cur = cur.right

        return result

if __name__ == '__main__':
    from tools.analysis import analysis_tree
    print(Solution().preorderTraversal(analysis_tree([1, None, 2, None, None, 3])))