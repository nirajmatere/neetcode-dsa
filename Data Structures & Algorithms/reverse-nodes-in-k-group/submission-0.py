# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        
        tempHead = head
        step = k
        while tempHead and step > 1:
            tempHead = tempHead.next
            step -= 1
        if not tempHead or step >= 2:
            return head
        nextHead = tempHead.next
        tempHead.next = None
        ansHead = reverseList(head)
        lastNode = head
        while nextHead:
            tempHead = nextHead
            step = k
            while tempHead and step > 1:
                tempHead = tempHead.next
                step -= 1
            if not tempHead or step >= 2:
                break     
            newNextHead = tempHead.next
            tempHead.next = None
            node = reverseList(nextHead)
            lastNode.next = node
            lastNode = nextHead
            nextHead = newNextHead
        
        lastNode.next = nextHead

        return ansHead







