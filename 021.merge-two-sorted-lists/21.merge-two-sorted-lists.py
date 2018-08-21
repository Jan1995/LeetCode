#关注小詹学python
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        #指向头指针
        head = dummy = ListNode(-1)
        #当两个链表都不为空的时候，比较大小，小的接在目标链表后，并该链表指针后移
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        #这里是当有一个链表后移到了最后，则将剩余一个全部接在目标链表后
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next
```
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        #关键在这 ，递归调用，参数改为某链表的l.next和另一个链表
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```