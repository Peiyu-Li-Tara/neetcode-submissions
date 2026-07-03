class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        rotten, fresh = set(), set()
        q = deque()
        directions = [
            [0, 1], [0, -1], [1, 0], [-1, 0]
        ]

        def bfs():
            min_time = -1
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if min(new_r, new_c) < 0 or new_r == R or new_c == C or (new_r, new_c) in rotten or grid[new_r][new_c] != 1:
                            continue
                        q.append((new_r, new_c))
                        rotten.add((new_r, new_c))
                        fresh.remove((new_r, new_c))
                min_time += 1
            return min_time
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                    rotten.add((r, c))
                if grid[r][c] == 1:
                    fresh.add((r, c))
        if not fresh:
            return 0

        min_time = bfs()
        return min_time if not fresh else -1