class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.indexMap = {}
        self.length = len(wordsDict)
        for i in range(self.length):
            if wordsDict[i] not in self.indexMap:
                self.indexMap[wordsDict[i]] = deque()
            self.indexMap[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        q1, q2 = self.indexMap[word1], self.indexMap[word2]
        min_path = self.length
        for i in q1:
            for j in q2:
                min_path = min(min_path, abs(j - i))
        return min_path
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
