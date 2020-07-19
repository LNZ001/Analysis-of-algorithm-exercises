from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        find_node = False
        dp = []
        cur = None

        pos = 0
        queue = [root]
        while not find_node and queue:
            for i in range(len(queue)):
                head = queue.pop()
                if pos == 0:
                    dp.append()










        # min_dp = "ffffffffffffffffffffffff"
        # while not find_node and root:
        #
        #     length = len(queue)
        #     for i in range(length):
        #         head = queue.pop()
        #         if pos == 0:
        #             dp.append(head.val)
        #
        #         else:
        #             dp[pos] = head.val + dp[pos-1//2]
        #
        #         if root
        #             min_dp = min(min_dp, dp[pos])
        #
        #         if
        #         pos += 1



        pass

if __name__ == '__main__':
    print(Solution().smallestFromLeaf())