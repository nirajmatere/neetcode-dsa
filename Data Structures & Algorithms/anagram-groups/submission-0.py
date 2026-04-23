class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if len(strs) == 1:
        #     return list(strs)
        
        anagrams = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            anagrams[key].append(s)

        answer = []
        for anagram_strings in anagrams.values():
            answer.append(anagram_strings)
        return answer