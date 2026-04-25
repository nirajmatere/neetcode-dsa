# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # root_idx = inorder.index(preorder[0])
        
        # root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        # root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])

        # return root

        idx_map = {}
        for i in range(len(inorder)):
            idx_map[inorder[i]] = i
        
        self.root_index = 0
        
        def dfs(left, right):
            if left > right:
                return None
            
            root = TreeNode(preorder[self.root_index])
            self.root_index += 1

            root_idx = idx_map[root.val]
            root.left = dfs(left, root_idx-1)
            root.right = dfs(root_idx+1, right)

            return root
        
        return dfs(0, len(inorder)-1)

            

            


        



        