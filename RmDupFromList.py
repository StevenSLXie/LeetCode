# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        cur = head
        while cur != None:
            while cur.next!= None and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
        
