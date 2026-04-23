class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = []
        for i in range(len(position)):
            pair = [position[i], float((target-position[i])/speed[i])]
            pos_time.append(pair)
        
        pos_time.sort(key=lambda x:x[0],reverse=True)
        print(pos_time)

        fleets = 0
        time = -1
        for x in pos_time:
            print(x)
            if x[1] > time:
                time = x[1]
                fleets += 1
        return fleets

