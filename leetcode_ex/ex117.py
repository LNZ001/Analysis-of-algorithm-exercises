from typing import List

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        init = root
        after_left = None
        pre = None
        while root:
            # ########## 记录下一次个深度的起点 ##########
            if after_left is None and (root.left or root.right):
                after_left = root.left if root.left is not None else root.right

            # ########## left+right都有的需要链接两者, 有至少一个的需要记录新的前和后, 链接前面. ##########
            if root.left and root.right:
                root.left.next = root.right
                if pre is not None:
                    pre.next = root.left
                    pre = root.right
            elif root.left is not None and pre is not None:
                pre.next = root.left
                pre = root.left
            elif root.right is not None and pre is not None:
                pre.next = root.right
                pre = root.right
            root = root.next

        if after_left is None:
            return init

        self.connect(after_left)
        return init


if __name__ == '__main__':
    node = Node(1, Node(2, Node(4),Node(5)), Node(3, Node(7)))
    print(Solution().connect(node))