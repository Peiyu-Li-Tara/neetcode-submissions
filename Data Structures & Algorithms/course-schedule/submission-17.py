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
            taken, q = set(), deque()
            visited = set()
            visited.add(course)
            q.append(course)
            while q:
                for _ in range(len(q)):
                    c = q.popleft()
                    for pre in graph[c]:
                        if pre in taken:
                            # print(course, c, pre)
                            return False
                        visited.add(pre)
                        q.append(pre)
                    taken.add(c)
            return True
        
        for i in range(numCourses):
            if not bfs(i):
                return False
        return True
