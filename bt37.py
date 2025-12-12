def check_row(board, r, ch):
    for i in range(9):
        if board[r][i] == ch:
            return False
    return True

def check_col(board, c, ch):
    for i in range(9):
        if board[i][c] == ch:
            return False
    return True

def check_box(board, r, c, ch):
    startRow, startCol = 3 * (r // 3), 3 * (c // 3)
    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            if board[i][j] == ch:
                return False
    return True

def is_valid(board, r, c, ch):
    return check_row(board, r, ch) and check_col(board, c, ch) and check_box(board, r, c, ch)

def backtrack(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                for ch in "123456789":
                    if is_valid(board, i, j, ch):
                        board[i][j] = ch
                        if backtrack(board):
                            return True
                        board[i][j] = "."
                return False
    return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    backtrack(board)
    for row in board:
        print(row)