# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p_root, q_root):
            if not p_root and not q_root:
                return True

            if (p_root and not q_root) or (not p_root and q_root):
                return False
            
            if p_root and q_root and p_root.val != q_root.val:
                return False
            
            left_decision = dfs(p_root.left, q_root.left)
            right_decision = dfs(p_root.right, q_root.right)

            return (left_decision and right_decision)
        
        return dfs(p, q)
        
