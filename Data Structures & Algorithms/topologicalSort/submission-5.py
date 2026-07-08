class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # if not edges:
        #     return [i for i in range(n)]

        # create adj list
        adj = {n: [] for n in range(n)}
        for prev, nxt in edges:
            adj[prev].append(nxt)
        
        visit = set() # visited nodes
        path = set() # Node being visited in the curr dfs call
        ret = []
        def dfs(node):
            if node in visit:
                return True
            if node in path:
                return False
            path.add(node)
            for nxt in adj[node]:
                if not dfs(nxt):
                    return False
            path.remove(node)
            visit.add(node)
            ret.append(node)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        ret.reverse()
        return ret
            
            