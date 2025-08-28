from base_config import BaseConfig
from utils import pawn_moves, print_board, king_moves, queen_moves




def main():
    piece =input("Enter piece (Pawn, King, Queen): ").capitalize()
    position =input("Enter position (example: B2): ").upper()

    if piece not in BaseConfig.OPTIONS_LIST:
        print("Invalid piece input")
        return
    if len(position) != 2 or position[0] not in BaseConfig.CHESS_BOARD_ALPHA_OPTIONS or position[1] not in BaseConfig.CHESS_BOARD_NUMERIC_OPTIONS:
        print("Invalid position input")
        return

    if piece == "Pawn":
        moves = pawn_moves(position)
        print(moves)
    elif piece == "King":
        moves = king_moves(position)
        print(moves)
    elif piece == "Queen":
        moves = queen_moves(position)
        print(moves)

    print_board(moves, position)


if __name__ == '__main__':
    main()