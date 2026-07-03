# class Solution:
#     def shortestPath(self, grid: List[List[int]]) -> int:
#         R, C = len(grid), len(grid[0])
#         visited, queue = set(), deque()
#         visited.add((0, 0))
#         queue.append((0, 0))
#         curr_len = 0
#         while queue:
#             for _ in range(len(queue)):
#                 r, c = queue.popleft()
#                 if r == R - 1 and c == C - 1:
#                     return curr_len
                
#                 direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#                 for dr, dc in direction:
#                     new_r, new_c = r + dr, c + dc
#                     if min(new_r, new_c) < 0 or new_r == R or new_c == C or grid[new_r][new_c] in visited or grid[new_r][new_c] == 1:
#                         continue
#                     visited.add((new_r, new_c))
#                     queue.append((new_r, new_c))
#             curr_len += 1
#         return -1
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        return -1