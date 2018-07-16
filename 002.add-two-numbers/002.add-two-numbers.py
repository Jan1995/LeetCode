微信公众号：小詹学python
第二题：add two numbers
错误示范：
def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len_max = max(len(l1),len(l2))
        add_ = 0
        for i in range(len_max):
            l3[i] = l1[i] + l2[i] + add_
            if l1[i] + l2[i] > 10:
                add_ = 1
            else:
                add_ = 0
                
        return l3
链表不是列表或数组，len()不适用
没考虑到链表长度不一致的情形！


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # maybe standard version
    def _addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(-1)
        carry = 0
        while l1 and l2:
            p.next = ListNode(l1.val + l2.val + carry)
            carry = p.next.val / 10
            p.next.val %= 10
            p = p.next
            l1 = l1.next
            l2 = l2.next
        
        res = l1 or l2
        while res:
            p.next = ListNode(res.val + carry)
            carry = p.next.val / 10
            p.next.val %= 10
            p = p.next
            res = res.next
        if carry:
            p.next = ListNode(1)
        return dummy.next
    
    # shorter version
    def addTwoNumbers(self, l1, l2):
        p = dummy = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            carry = val / 10
            p.next = ListNode(val % 10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            p = p.next
        return dummy.next
            

#链表python构建
# -*- coding:utf8 -*-
#/usr/bin/env python

class Node(object):
    def __init__(self, data, pnext = None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        return str(self.data)

class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print "this chain table is empty."
            return

        if index < 0 or index >= self.length:
            print 'error: out of index'
            return

        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev._next = node._next
            self.length -= 1

    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print "this chain tabale is empty"
            return

        if index < 0 or index >= self.length:
            print "error: out of index"
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print 'error: out of index'
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print "error: out of index"
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        return node.data


    def getIndex(self, data):
        j = 0
        if self.isEmpty():
            print "this chain table is empty"
            return
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print "%s not found" % str(data)
            return

    def clear(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return "empty chain table"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print "error: out of index"
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print "error: out of index"
            return
        self.update(ind, val)

    def __len__(self):
        return self.length

python链表
        