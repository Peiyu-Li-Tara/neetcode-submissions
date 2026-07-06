class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_map = {i: [] for i in range(1, n + 1)}
        for pre, nxt in relations:
            adj_map[pre].append(nxt)
        
        visited = set()
        cache = {}

        def dfs(course):
            if course in cache:
                return cache[course]
            if not adj_map[course]:
                cache[course] = 1
                return 1
            if course in visited:
                return -1
            
            visited.add(course)
            max_cnt = 0
            for nxt in adj_map[course]:
                cnt = dfs(nxt)
                if cnt == -1:
                    return -1
                max_cnt = max(max_cnt, cnt)
            visited.remove(course)
            cache[course] = max_cnt + 1
            return max_cnt + 1
        
        sem = 0
        for course in adj_map:
            tmp = dfs(course)
            if tmp == -1:
                return -1
            sem = max(sem, tmp)
        return sem


        