# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # self.count = k
        # self.rootVal = root.val
        
        # def dfs(root):
        #     if not root:
        #         return 
            
        #     dfs(root.left)
        #     self.count -= 1

        #     if self.count == 0:
        #         self.rootVal = root.val
        #         return self.rootVal
        #     dfs(root.right)
        
        # dfs(root)
        # return self.rootVal

        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]

        