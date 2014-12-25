# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        s1 = l1
        s2 = l2
        sum = ListNode(0)
        head = sum
        flag = 0
        while 1:
            
            head.val = s1.val + s2.val + flag
            if head.val >= 10:
                flag = 1
                head.val -= 10
            else:
                flag = 0
            s1 = s1.next
            s2 = s2.next
            
            if s1 == None and s2 == None and flag == 0:
                return sum
            if s1 == None:
                s1 = ListNode(0)
            if s2 == None:
                s2 = ListNode(0)
            head.next = ListNode(0)
            head = head.next
            
        return sum
