class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for prv, nxt in prerequisites:
            adj[prv].append(nxt)
        
        ret = []
        path = set()
        cache = {}
        def dfs(i):
            if i in cache: return cache[i]
            # if not adj[i]: return True
            if i in path: return False

            path.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            path.remove(i)
            
            cache[i] = True
            ret.append(i)
            return cache[i]
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return ret