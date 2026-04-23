class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c)-ord('a')] += 1
            hashmap[str(arr)].append(s)

        return list(hashmap.values())
            

            