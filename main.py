from generate_board import generate_board
from save_load_gameboard import save_game_board_to_json
import interface


def main():
    board = generate_board(4, 5, 2)
    with open("new.json", "w") as fp:
        save_game_board_to_json(fp, board)
    interface.main_loop(board)
    with open("finished.json", "w") as fp:
        save_game_board_to_json(fp, board)


if __name__ == "__main__":
    main()
