# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        virtual = ListNode(-1111)   # some dummy vaue as the header
        virtual.next = head
        dummy_head = virtual  # dummy head, always point to the header
        flag = False

        while virtual is not None:
            if isNone(virtual.next):
                return dummy_head.next
              
            cur = virtual.next
    
            while not isNone(cur.next) and check_equal(cur.val,cur.next.val):
                cur.next = change_pointer(cur.next.next)
                flag = True
              
            if not flag:
                # if no duplicated value in this round of searching, proceed to the next one
                virtual = move_pointer(virtual)
            else:
                # if there is duplicated value, change the next pointer
                virtual.next = change_pointer(cur.next)
            flag = False
            
        return dummy_head.next
            
def move_pointer(virtual):
    return virtual.next
        
def change_pointer(new_P):
    return new_P
        
def check_equal(val_A, val_B):
    return val_A == val_B 
        
def isNone(a):
    if a is None:
        return True
    else:
        return False
