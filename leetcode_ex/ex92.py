
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        init = ListNode(None)
        init.next = head

        pos = 1

        ll = init
        while pos < m:
            pos += 1
            ll = head
            head = head.next

        # ll, lr   rl, rr
        rl = head
        last_p = None
        while pos < n:
            # 记录下一节点
            next_p = head.next

            # 反转链表
            if last_p is not None:
                head.next = last_p

            # 准备更新
            last_p = head
            pos += 1

            # 跳转到下一节点.
            head = next_p


        # 记录末尾
        lr = head
        rr = head.next

        head.next = last_p

        # 链接
        ll.next = lr
        rl.next = rr

        return init.next



if __name__ == '__main__':
    tests = [3, 5]
    tests.reverse()
    p = None
    for t in tests:
        p = ListNode(t, p)
    print(Solution().reverseBetween(p, 1, 2))