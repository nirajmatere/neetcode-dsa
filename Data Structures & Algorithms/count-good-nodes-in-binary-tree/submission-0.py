# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 1
        q = collections.deque()
        maxval = root.val
        q.append([root, root.val])
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node[0].left:
                    nodeVal = node[0].left.val
                    if nodeVal >= node[1]:
                        count += 1
                        q.append([node[0].left, nodeVal])
                    else:
                        q.append([node[0].left, node[1]])
                if node[0].right:
                    nodeVal = node[0].right.val
                    if nodeVal >= node[1]:
                        count += 1
                        q.append([node[0].right, nodeVal])
                    else:
                         q.append([node[0].right, node[1]])
        
        return count




        