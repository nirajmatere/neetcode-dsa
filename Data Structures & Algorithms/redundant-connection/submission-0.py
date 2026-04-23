class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)
    
        def findParent(n):
            if n != parent[n]:
                parent[n] = findParent(parent[n])
            return parent[n]


        def solve(n1, n2):
            parent1, parent2 = findParent(n1), findParent(n2)

            if parent1 == parent2:
                return False

            if rank[parent1] >= rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True


        for n1,n2 in edges:
            if not solve(n1,n2):
                return [n1,n2]
