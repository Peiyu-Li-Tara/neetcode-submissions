class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # ["practice","makes","perfect","coding","alow","coding","makes","mad"]
        # makes: [1, 6]
        # coding: [3, 5]
        # [1, 3, 5, 6] , 2, 4, 1

        q1, q2 = [], []
        ret = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                q1.append(i)
                currDist = i - q2[-1] if q2 else ret
                ret = min(currDist, ret)
            elif wordsDict[i] == word2:
                q2.append(i)
                currDist = i - q1[-1] if q1 else ret
                ret = min(currDist, ret)
        return ret
            

        