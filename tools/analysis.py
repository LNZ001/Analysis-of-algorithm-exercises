# ########## 用于快速解析输出测试用例结构. ##########

# Definition for a binary tree node.
# 需要结合实际进行替换.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def analysis_tree(node_list):
    if len(node_list) == 0: return None
    length = len(node_list)
    node_list = [TreeNode(n) if n is not None else None for n in node_list]

    for i in range(length):
        if node_list[i] is None:
            continue

        left = i*2+1
        right = left + 1
        if left < length:
            node_list[i].left = node_list[left]
            if right < length:
                node_list[i].right = node_list[right]

        else:
            return node_list[0]

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def analysis_listnode(nodes):
    if isinstance(nodes, str):
        '''->拼接的.'''
        node_list = nodes.split("->")
    else:
        node_list = nodes
    if len(node_list) ==0: return None
    res = None
    for i in range(len(node_list)-1, -1, -1):
        res = ListNode(node_list[i], res)
    return res

if __name__ == '__main__':
    # analysis_tree([1, None, 2, None, None, 3])
    analysis_listnode("-1->5->3->4->0")