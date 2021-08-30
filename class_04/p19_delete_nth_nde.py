# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        left = right = head
        for i in range(n):
            right = right.next
        if not right:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         self.size = self.getIndex(head)
#         curnt = head
#         if curnt.next == None:
#             curnt.val = ''
#             return head
#
#         index = self.size - n
#         self.size -= 1
#         for i in range(index):
#             curnt = curnt.next
#         curnt.next = curnt.next.next
#         return head
#
#     def getIndex(self, head):
#         self.size = 0
#         while head.next != None:
#             head = head.next
#             self.size += 1
#         return self.size