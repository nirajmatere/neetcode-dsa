# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)-1):
                node = q.popleft()
                if node:
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)

            if q: 
                node = q.popleft()
                if node:
                    ans.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                    
        
        return ans


