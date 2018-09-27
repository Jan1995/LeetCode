```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        cur = dummy = ListNode(0)
        cur.next = head
        while cur.next and cur.next.next:#循环终止条件：后续不够两个节点进行交换
            #这就是上述图片的实现，关键所在
            cur.next.next.next, cur.next.next, cur.next, cur = \
            cur.next, cur.next.next.next, cur.next.next, cur.next
        return dummy.next
    

```

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverseList(head, k):
            pre = None
            cur = head
            while cur and k > 0:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
                k -= 1
            head.next = cur
            return cur, pre

        if not head or not head.next:
            return head
        ret = head.next
        p = head
        pre = None
        while p:
            next, newHead = reverseList(p, 2)
            if pre:
                pre.next = newHead
            pre = p
            p = next
        return ret