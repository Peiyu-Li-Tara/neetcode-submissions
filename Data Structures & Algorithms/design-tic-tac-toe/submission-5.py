class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.n = n
        self.directions = [
            [0, 1],
            [1, 0],
            [1, 1],
            [-1, 1]
        ]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        def count(r, c, dr, dc):
            cnt = 0
            while 0 <= r < self.n and 0 <= c < self.n:
                if self.board[r][c] != player:
                    print(r, c, self.board[r][c])
                    break
                else:
                    cnt += 1
                    r += dr
                    c += dc
            return cnt
        
        for dr, dc in self.directions:
            cnt = 1 + count(row + dr, col + dc, dr, dc) + count(row - dr, col - dc, -dr, -dc)
            if cnt == self.n:
                return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
