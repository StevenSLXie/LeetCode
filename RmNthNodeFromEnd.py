# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        traverse = 1
        cur = head
        while cur.next != None:
            cur = cur.next
            traverse += 1
        
        if traverse == n:
            return head.next
        
        cur = head
        i = traverse - n -1 
        while i>0:
            cur = cur.next
            i -= 1
        if n == 1:
            cur.next = None
        else:
            cur.next = cur.next.next
        return head
        
