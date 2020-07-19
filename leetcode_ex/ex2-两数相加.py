# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    递归
    '''
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #
    #     up = 0
    #     node = ListNode(None)
    #     head = node
    #     while l1 and l2:
    #         val = (l1.val + l2.val + up) % 10
    #         up = (l1.val + l2.val + up)//10
    #
    #         l1 = l1.next
    #         l2 = l2.next
    #         node.next = ListNode(val)
    #         node = node.next
    #
    #     l_next = l1 if l1 else l2
    #     while l_next:
    #         val = (l_next.val + up) % 10
    #         up = (l_next.val + up) // 10
    #
    #         l_next = l_next.next
    #         node.next = ListNode(val)
    #         node = node.next
    #
    #     if up == 1:
    #         node.next = ListNode(1)
    #
    #     return head.next

    '''
    迭代
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addTwo(l1, l2)

    def addTwo(self, l1, l2, up=0):
        if not l1 and not l2: return ListNode(1) if up == 1 else None
        if not l1 or not l2:
            head = l1 if not l2 else l2
            cur = head
            while True:
                val = (cur.val + up) % 10
                up = (cur.val + up) // 10
                cur.val = val
                if cur.next is None:
                    if up == 1: cur.next = ListNode(1)
                    break

                cur = cur.next
            return head

        val = (l1.val + l2.val + up) % 10
        up = (l1.val + l2.val + up) // 10
        v = ListNode(val)
        v.next = self.addTwo(l1.next, l2.next, up)
        return v

if __name__ == '__main__':
    from tools.analysis import analysis_listnode
    print(Solution().addTwoNumbers(analysis_listnode([0]), analysis_listnode([7, 3])))