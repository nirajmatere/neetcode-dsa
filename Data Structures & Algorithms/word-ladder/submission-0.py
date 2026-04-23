class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word) 
        
        q = deque()
        visited = set()
        count = 1
        q.append(beginWord)
        visited.add(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            
            count += 1
        
        return 0
