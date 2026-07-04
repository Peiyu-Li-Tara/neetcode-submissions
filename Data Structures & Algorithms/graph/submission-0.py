class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        self.graph[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph.keys() or dst not in self.graph.keys() or dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.graph.keys() or dst not in self.graph.keys():
            return False
        if dst in self.graph[src]:
            return True
        visited, q = set(), deque()
        visited.add(src)
        q.append(src)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for v in self.graph[node]:
                    if v == dst:
                        return True
                    q.append(v)
                    visited.add(v)
        return False
                
        

