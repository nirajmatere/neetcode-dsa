# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first, second = head, head

        for i in range(n):
            second = second.next
        
        if second == None:
            return head.next
        
        while second.next:
            second = second.next
            first = first.next
        
        if first.next != None:
            first.next = first.next.next
        
        return head
