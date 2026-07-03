class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        R, C = len(grid), len(grid[0])
        visited, q = set(), deque()
        visited.add((0, 0))
        q.append((0, 0))
        length = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == R - 1 and c == C - 1:
                    return length
                directions = [
                    [0, 1],
                    [0, -1],
                    [1, 0],
                    [-1, 0],
                    [-1, -1],
                    [1, -1],
                    [-1, 1],
                    [1, 1]
                ]

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if min(new_r, new_c) < 0 or new_r == R or new_c == C or (new_r, new_c) in visited or grid[new_r][new_c] == 1:
                        continue
                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))
            length += 1
        return -1







