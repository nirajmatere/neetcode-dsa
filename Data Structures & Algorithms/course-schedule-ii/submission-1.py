class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        course_pre_map = {}
        for i in range(numCourses):
            course_pre_map[i] = []
        
        for i in pre:
            course_pre_map[i[0]].append(i[1])
        
        path = set()
        order = []
        def dfs(node):
            if node in path:
                return False
            path.add(node)

            for x in course_pre_map[node]:
                if not dfs(x):
                    return False
            path.remove(node)
            course_pre_map[node] = []
            if node not in order:
                order.append(node)
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return []
        # print(order)
        return order