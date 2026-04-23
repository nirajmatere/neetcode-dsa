class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq = {}
        for c in s1:
            freq[c] = 1 + freq.get(c, 0)
        
        left = 0
        
        copy_freq = freq.copy()
        for i in range(len(s2)):
            # print('s2[i]:', s2[i])
            if copy_freq.get(s2[i],0) == 0:
                # print('letter not exist')
                # if s2[left] != s2[i]:
                #     copy_freq[s2[left]] = freq.get(s2[left],0)
                if freq.get(s2[i],0) == 0:
                    copy_freq = freq.copy()
                elif freq.get(s2[left],0) != 0:
                    if s2[left] != s2[i]:
                        copy_freq[s2[left]] = copy_freq.get(s2[left],0) + 1
                left += 1
                
            else:
                # print('letter exist')
                copy_freq[s2[i]] = copy_freq.get(s2[i],0) - 1
                if sum(copy_freq.values()) == 0:
                    return True
            # print('copy_freq:', copy_freq)
        return False
            

        