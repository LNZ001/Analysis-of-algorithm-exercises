from typing import List
from tools.analysis import analysis_listnode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         root = ListNode(None)
#
#         cur = None
#         while head:
#             if cur is not None and cur.val is not None and cur.val <= head.val:
#                 pass
#             else:
#                 cur = root
#
#
#             while cur.next and head.val >= cur.next.val:
#                 cur = cur.next
#
#             next_head = head.next
#             tmp = cur.next
#             cur.next = head
#             head.next = tmp
#             head = next_head
#
#
#         return root.next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur, nxt = head, head.next
        dummy = ListNode(float('-inf'))
        dummy.next = head
        while nxt:
            if nxt.val >= cur.val:
                cur, nxt = nxt, nxt.next
            else:
                cur.next = nxt.next
                pre1, pre2 = dummy, dummy.next
                while nxt.val > pre2.val:
                    pre1, pre2 = pre2, pre2.next
                pre1.next = nxt
                nxt.next = pre2
                nxt = cur.next
        return dummy.next

if __name__ == '__main__':
    print(Solution().insertionSortList(analysis_listnode("-1->5->3->4->0")))