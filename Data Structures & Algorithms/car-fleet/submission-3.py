class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleet = 0
        sorted_stack = []

        for i in range(len(position)):
            sorted_stack.append([position[i], speed[i]])
        
        sorted_stack = sorted(sorted_stack, key=lambda x: x[0])
        for i in range(len(sorted_stack)):
            pos, spe = sorted_stack[-1]
            sorted_stack.pop()
            if not stack:
                time = (target - pos) / spe
                stack.append([spe, time])
                fleet += 1
            else:
                if spe <= stack[-1][0]:
                    fleet += 1
                    time = (target-pos) / spe
                    stack.append([spe, time])
                else:
                    time = (target-pos) / spe
                    if time > stack[-1][1]:
                        fleet += 1
                        stack.append([spe, time])

        return fleet