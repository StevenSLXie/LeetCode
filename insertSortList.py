# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
            
        fh = ListNode(0)
        fh.next = head
        cur = head
        # ptr = ptr.next
        
        # 1 2 3 5 7 8 4 9
        # move the pre until a value larger than cur.next is found
        # then change the link
        # save the cur.next
        # point cur.next as cur.next.next (skip the moved one)
        # point cur.next.next as pre.next
        # pre.next is now the cur.next
        
        while cur.next:
            if cur.next.val < cur.val:
                pre = fh
                while pre.next.val <= cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                cur = cur.next
        return fh.next
            
            
        
        
