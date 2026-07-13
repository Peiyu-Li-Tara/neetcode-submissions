class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        cur_player = 1 if player == 1 else -1
        self.row[row] += cur_player
        self.col[col] += cur_player
        if row == col:
            self.diagonal += cur_player
        if row == self.n - 1 - col:
            self.antidiagonal += cur_player
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diagonal) == self.n or abs(self.antidiagonal) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
