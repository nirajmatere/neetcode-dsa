# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        if k == 1:
            return lists[1]
        
        # # solution with extra array O(n) space
        # array = []
        # for li in lists:
        #     head = li
        #     while head:
        #         array.append(head.val)
        #         head = head.next
        
        # # print(array)
        # array.sort()
        # newHead = ListNode(array[0])
        # temp = newHead
        # for i in range(1, len(array)):
        #     node = ListNode(array[i])
        #     temp.next = node
        #     temp = temp.next
        
        # return newHead

        pointers = []
        for i in range(k):
            pointers.append(i)
        
        n = 0
        for ll in lists:
            head = ll
            while head:
                n += 1
                head = head.next
        # print(n)
        headNode = ListNode(0)
        temp = headNode
        for i in range(n):
            min_pointer = 0
            node_val = float('inf')
            for pointer in range(len(pointers)):
                if lists[pointer] and lists[pointer].val < node_val:
                    node_val = lists[pointer].val
                    min_pointer = pointer
            node = ListNode(node_val)
            lists[min_pointer] = lists[min_pointer].next
            temp.next = node
            temp = temp.next
        
        return headNode.next








