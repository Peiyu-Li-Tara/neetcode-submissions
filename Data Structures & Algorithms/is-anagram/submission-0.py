class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        for i in s:
            if i in charMap.keys():
                charMap[i] += 1
            else:
                charMap[i] = 1
        
        for j in t:
            if j not in charMap.keys():
                return False
            charMap[j] -= 1
        
        for k in charMap.keys():
            if charMap[k] != 0:
                return False
        return True