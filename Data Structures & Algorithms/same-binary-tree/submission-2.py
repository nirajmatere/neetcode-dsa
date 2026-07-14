# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False

        check = True
        def dfs(p, q) -> bool:
            if p and q and p.val != q.val:
                return False
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False

            left_check = dfs(p.left, q.left)
            if not left_check:
                check = False
                return False
            right_check = dfs(p.right, q.right)
            if not right_check:
                check = False
                return False

            return True

        if not check:
            return False
        else:
            return dfs(p, q)





