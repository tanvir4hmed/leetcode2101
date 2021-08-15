# Runtime: 284 ms, faster than 53.86% of Python online submissions for Design Linked List.
# Memory Usage: 14.1 MB, less than 53.25% of Python online submissions for Design Linked List.

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        self.size += 1
        curnt = self.head
        for i in range(index):
            curnt = curnt.next
        new = ListNode(val)
        new.next = curnt.next
        curnt.next = new

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        curnt = self.head
        for i in range(index):
            curnt = curnt.next
        curnt.next = curnt.next.next

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curnt = self.head
        for i in range(index + 1):
            curnt = curnt.next
        return curnt.val
