# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False

        def isSameTree(p,q):
            if p and q and p.val != q.val:
                return False
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            
            left_check = isSameTree(p.left, q.left)
            if not left_check:
                return False
            right_check = isSameTree(p.right, q.right)
            
            return left_check and right_check

        def dfs(p, q):
            if not q:
                return True
            if not p and q:
                return False
                
            if p.val == q.val:
                check = isSameTree(p,q)
                if check:
                    return True
            return dfs(p.left, q) or dfs(p.right, q)
        
        return dfs(root, subRoot)






