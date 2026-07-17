class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for prv, nxt in prerequisites:
            adj[prv].append(nxt)
        
        ret = []
        visited, path = set(), set()
        def dfs(i):
            if i in visited: return True
            if i in path: return False

            path.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            path.remove(i)
            visited.add(i)
            ret.append(i)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return ret