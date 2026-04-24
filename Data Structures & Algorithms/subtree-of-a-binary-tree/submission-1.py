# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root1, root2):
            isSame = True
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (root1 and not root2):
                return False
            if root1.val != root2.val:
                return False
            
            left = isSameTree(root1.left, root2.left)
            if not left:
                return False
            right = isSameTree(root1.right, root2.right)

            return left and right
        
        if root and subRoot and root.val == subRoot.val:
            decision = isSameTree(root, subRoot)
            if decision:
                return True
        
        if root: 
            left = self.isSubtree(root.left, subRoot)
            if left:
                return True
        if root: 
            right = self.isSubtree(root.right, subRoot)
            if right:
                return True
        
        return False

            
            