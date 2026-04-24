# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.count = k
        # self.ans = root.val

        # def dfs(root):
        #     if not root:
        #         return
            
        #     dfs(root.left)
        #     if self.count == 0:
        #         return
        #     self.count -= 1
        #     if self.count == 0:
        #         self.ans = root.val
        #         return
        #     dfs(root.right)
        
        # dfs(root)
        # return self.ans

        arr = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            arr.append(root.val)
            if len(arr) == k:
                return
            dfs(root.right)
        
        dfs(root)
        return arr[k-1]