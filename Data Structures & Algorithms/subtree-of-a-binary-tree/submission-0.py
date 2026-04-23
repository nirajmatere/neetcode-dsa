# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and not subRoot) or not subRoot:
            return True

        if not root and subRoot:
            return False

        # code from Same Binary Tree Problem
        def isSameTree(p, q):
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
    
        if root.val == subRoot.val:
            check = isSameTree(root, subRoot)
            if check:
                return True

        check_left = self.isSubtree(root.left, subRoot)
        check_right = self.isSubtree(root.right, subRoot)

        return check_left or check_right

        
