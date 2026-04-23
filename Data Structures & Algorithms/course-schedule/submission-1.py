class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        course_pre_map = {}
        for i in range(numCourses):
            course_pre_map[i] = []
        
        for i in pre:
            course_pre_map[i[0]].append(i[1])
        
        path = set()
        def dfs(node):
            if node in path:
                return False
            path.add(node)

            for x in course_pre_map[node]:
                if not dfs(x):
                    return False
            path.remove(node)
            course_pre_map[node] = []
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

                    

        
        