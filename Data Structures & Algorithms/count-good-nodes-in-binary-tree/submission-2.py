# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good = 0
        max_ = root.val
        q = deque()
        q.append([root, max_])
        while q:
            for _ in range(len(q)):
                pair = q.popleft()
                node = pair[0]
                max_ = pair[1]
                
                if node:
                    if node.val >= max_:
                        good += 1
                        max_ = node.val
                    if node.left: 
                        q.append([node.left, max_])
                    if node.right:
                        q.append([node.right, max_])
                
        return good