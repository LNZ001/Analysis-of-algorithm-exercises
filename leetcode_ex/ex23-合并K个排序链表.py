from typing import List
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


def lt(self, other):
    return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None
        for i in range(len(lists)-1, -1, -1):
            if lists[i] is None:
                lists.pop(i)
        if len(lists) == 0: return None
        setattr(type(lists[0]), "__lt__", lt)

        queue = PriorityQueue(maxsize=len(lists))
        head = ListNode(-1)
        cur = head

        for list in lists:
            queue.put(list)

        while not queue.empty():
            q = queue.get()
            cur.next = q
            cur = cur.next

            if q.next is not None:
                queue.put(q.next)

        return head.next



if __name__ == '__main__':
    from tools.analysis import analysis_listnode
    print(Solution().mergeKLists([analysis_listnode([1,4 ,5 ]),
                                  analysis_listnode([1, 3, 4]),
                                  analysis_listnode([2, 6])]))