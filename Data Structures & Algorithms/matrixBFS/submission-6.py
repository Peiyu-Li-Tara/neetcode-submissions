class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited, queue = set(), deque()
        visited.add((0, 0))
        queue.append((0, 0))
        curr_len = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == R - 1 and c == C - 1:
                    return curr_len
                
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direction:
                    new_r, new_c = r + dr, c + dc
                    if min(new_r, new_c) < 0 or new_r == R or new_c == C or (new_r, new_c) in visited or grid[new_r][new_c] == 1:
                        continue
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))
            curr_len += 1
        return -1