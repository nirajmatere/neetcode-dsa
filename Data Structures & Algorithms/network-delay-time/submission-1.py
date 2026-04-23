class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        for node, nei, time in times:
            adj[node].append([nei,time])

        minTime = {}
        for i in range(n+1):
            minTime[i] = float('inf')
        minTime[k] = 0

        q = deque()
        q.append([k,0])

        while q:
            for i in range(len(q)):
                element = q.popleft()
                node, time = element[0], element[1]
                for nei, edge_cost in adj[node]:
                    cost = time + edge_cost
                    minTime[nei] = min(minTime[nei], cost)
                    if minTime[nei] >= cost:
                        q.append([nei,cost])
        
        print(minTime)
        req_time = 0
        for i in range(1, len(minTime)):
            if minTime[i] == float('inf'):
                return -1
            req_time = max(minTime[i], req_time)

        return req_time
        