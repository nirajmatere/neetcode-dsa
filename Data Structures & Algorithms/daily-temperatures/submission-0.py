class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                stack.append([temperatures[i],i])
                res.append(0)
            else:
                if temperatures[i] < stack[-1][0]:
                    res.append(stack[-1][1]-i)
                    stack.append([temperatures[i],i])
                else:
                    while stack and temperatures[i] >= stack[-1][0]:
                        stack.pop()
                    if not stack:
                        stack.append([temperatures[i],i])
                        res.append(0)
                    else:
                        res.append(stack[-1][1]-i)
                        stack.append([temperatures[i],i])
        
        return res[::-1]


