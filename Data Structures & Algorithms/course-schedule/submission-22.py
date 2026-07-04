class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        if len(prerequisites) == 1 and numCourses <= 1:
            return True

        # build the adjlist
        graph = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        print(graph)
        
        def bfs(course):
            visit, q = set(), deque()
            visit.add(course)
            q.append(course)
            while q:
                for _ in range(len(q)):
                    c = q.popleft()
                    for pre in graph[c]:
                        if pre in visit:
                            print(course, c, pre)
                            return False
                        q.append(pre)
                    visit.add(c)
            return True
        
        visit = set()
        def dfs(course):
            if not graph[course]:
                return True
            if course in visit:
                return False
            visit.add(course)
            for pre in graph[course]:
                if pre in visit:
                    return False
                dfs(pre)
            visit.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
