class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        self.size = self.getIndex(head)
        if head.next == None:
            return 0
        index = self.size - n
        self.size -= 1
        curnt = head
        for i in range(index):
            curnt = curnt.next
        curnt.next = curnt.next.next
        return head

    def getIndex(self, head):
        self.size = 0
        while head.next != None:
            head = head.next
            self.size += 1
        return self.size
