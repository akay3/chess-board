def is_valid_move(row, col):
    return 0 <= row < 8 and 0 <= col < 8

def get_position_row_col(position):
    row = 8 - int(position[1])
    column = ord(position[0]) - ord("A")
    return row, column

def pawn_moves(position):
    row, col = get_position_row_col(position)
    print(row, col)
    moves = []
    if is_valid_move(row -1, col):
        moves = [(row - 1, col)]
    return moves


def king_moves(position):
    moves = []
    row, col = get_position_row_col(position)
    possible_moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),            (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for _row, _col in possible_moves:
        r, c = row + _row, col + _col
        if is_valid_move(r, c):
            moves.append((r, c))
    return moves


def queen_moves(position):
    moves = []
    row, col = get_position_row_col(position)
    possible_moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),            (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for _row, _col in possible_moves:
        r, c = row + _row, col + _col
        while True:
            if is_valid_move(r, c):
                moves.append((r, c))
                r, c = r + _row, c + _col
            else:
                break
    return moves

def print_board(moves, position):
    board = []
    for row in range(8):
        empty_row = ["." for _ in range(8)]
        board.append(empty_row)

    for row, col in moves:
        board[row][col] = "*"

    # Get current position for the piece
    row,col = get_position_row_col(position)
    board[row][col] = "P"

    for row in board:
        print(*row)