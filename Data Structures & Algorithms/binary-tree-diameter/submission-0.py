# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        return 1 + max(self.maxPath(root.left), self.maxPath(root.right))
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        
        left = self.maxPath(root.left)
        right = self.maxPath(root.right)

        root_diameter = left + right

        return max(root_diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        



        
        



        