# solve sudoku puzzle using recursive backtracking algorithm
# puzzles will be in the format of a 2D array
# the function will return whether or not a solution is possible is if so, what the solution board is

def find_next_empty(board):
    # find the next position on the board that is not occupied (non occupied positions in the array will be represented by b)
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == b:
                return r, c

    return None, None #suggests that there is no room left

def is_valid(board, guess, row, column):

    # iterating through each row
    row_vals = board[row]
    if guess in row_vals:
        return False
    # iterating through each column
    col_vals = [board[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    # iterating through each 3 by 3 box

    row_start = row//3 * 3
    col_start = col//3 * 3


    for (r in range(row_start, row_start + 3)):
        for (c in range (col_start, col_start + 3)):
            if board[r][c] == guess:
                return False;

    # if these tests are passed, then the input guess is valid

def solve_sudoku(board):
    row, col = find_next_empty(board)

# case 1: since only valid inputs are allowed, if there is no more room, then the board must be solved
    if row is none:
        return True

# case 2: if an open spot is found, make a guess for the correct value
    for guess in range(1, 10):
        if is_valid(board, guess, row, column):
            # if the guess is valid, place the value into the board
            board[row][col] = guess
            # recursively call this function
            if solve_sudoku(board):
                return True
        # if the guess turned out not to be correct, we can backtrack and try a new number
        board[row][col] = b;

    # if none of the combinations satisfy the above conditions, then there is no solution
    return False

example_board = [
    [1, b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b, b],
    [b, b, b, 2, b, b, b, b, b],
    [b, b, 1, b, b, b, 5, b, b],
    [b, b, 3, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, 8, b, b],
    [b, b, 4, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b, 9]
]

print(solve_sudoku(example_board))