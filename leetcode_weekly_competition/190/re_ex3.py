class Solution(object):
    def pseudoPalindromicPaths (self, root):
        s = set()

        def dfs(root):
            if not root: return 0
            # ######### 置换 ###########
            if root.val in s:
                s.discard(root.val)
            else:
                s.add(root.val)

            res = dfs(root.left) + dfs(root.right)
            if not root.left and not root.right:
                res += len(s) <= 1

            # ######### 反置换 ###########
            if root.val in s:
                s.discard(root.val)
            else:
                s.add(root.val)

            return res

        return dfs(root)