# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = ''
        if not root:
            return tree
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                tree += '#'
                node = q.popleft()
                if node:
                    val = node.val
                    tree += str(node.val)

                    if node.left: 
                        q.append(node.left)
                    else:
                        q.append(None)
                    if node.right: 
                        q.append(node.right)
                    else:
                        q.append(None)
                else:
                    tree += 'null'
        # print(tree)
        return tree
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        # print(data)
        arr = []
        for i in range(len(data)):
            if data[i] == '#':
                # print("Inside")
                j = i
                i += 1
                while i < len(data) and data[i] != '#':
                    i += 1
                # print("i:",i,"j:",j)
                val = data[j+1:i]
                arr.append(val)
        # print(arr)
        root = TreeNode(int(arr[0]))
        q = deque([root])
        idx = 1
        while q:
            node = q.popleft()
            if arr[idx] != 'null':
                node.left = TreeNode(int(arr[idx]))
                q.append(node.left)
            idx += 1
            if arr[idx] != 'null':
                node.right = TreeNode(int(arr[idx]))
                q.append(node.right)
            idx += 1
        
        return root
            

    







