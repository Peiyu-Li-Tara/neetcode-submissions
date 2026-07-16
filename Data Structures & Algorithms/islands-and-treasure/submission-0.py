class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])

        q = deque()
        visited = {}
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
    
        directions = [
                    [0, 1],
                    [0, -1],
                    [1, 0],
                    [-1, 0]
                ]
        
        # BFS
        length = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if min(new_r, new_c) < 0 or new_r == R or new_c == C or grid[new_r][new_c] == -1 or grid[new_r][new_c] == 0 or (new_r, new_c) in visited:
                        continue
                    q.append((new_r, new_c))
                    visited[(new_r, new_c)] = length
            length += 1
        
        for r, c in visited.keys():
            grid[r][c] = visited[(r, c)]
                