class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sol1: Time: O(m * nlogn)
        # anagrams = defaultdict(list)
        # for s in strs:
        #     key = str(sorted(s))
        #     anagrams[key].append(s)

        # answer = []
        # for anagram_strings in anagrams.values():
        #     answer.append(anagram_strings)
        # return answer

        # sol2:
        anagrams = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for i in range(len(s)):
                key[ord(s[i]) - ord('a')] += 1
            anagrams[str(key)].append(s)

        # answer = []
        # for anagram_strings in anagrams.values():
        #     answer.append(anagram_strings)
        # return answer

        return list(anagrams.values())