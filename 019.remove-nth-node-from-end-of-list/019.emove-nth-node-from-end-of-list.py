#关注小詹学python
 ```
class Solution:
    #对应上边小詹说的第二种思路
    def removeNthFromEnd(self, head, n):
        first = second = head
        #将第一个‘指针’移动 n 个位置
        for _ in range(n):
            first = first.next
        #当极端情况，即first指向了最后一个节点，且要删的是第一个节点（倒数第n个）
        if not first:
            return head.next
        #将两个‘指针’同步后移
        #直到first指向了最后一个节点（两个‘指针’始终保持相同间隔）
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
```