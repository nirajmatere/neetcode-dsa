# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def bfs(root): 
            if not root:
                return []

            ans = []

            q = collections.deque()
            q.append(root)

            while q:
                temp_ans = []
                q_size = len(q)

                for i in range(q_size):
                    node = q.popleft()
                    if node:
                        temp_ans.append(node.val)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                
                if len(temp_ans) != 0:
                    ans.append(temp_ans)
                
            return ans      
                  
        ans = bfs(root)
        res = []
        for temp_ans in ans:
            res.append(temp_ans[-1])

        return res

