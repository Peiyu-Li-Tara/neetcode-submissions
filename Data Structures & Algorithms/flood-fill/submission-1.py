class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        R, C = len(image), len(image[0])
        original_color = image[sr][sc]
        def dfs(r, c):
            if min(r, c) < 0 or r == R or c == C or image[r][c] != original_color or (r, c) in visited:
                return
            if image[r][c] == original_color:
                image[r][c] = color
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            visited.remove((r, c))
            return
        dfs(sr, sc)
        return image