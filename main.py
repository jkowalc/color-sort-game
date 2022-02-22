from generate_board import generate_board
import interface
from config import init_config


def main():
    init_config()
    board = generate_board(3, 2, 2)
    interface.level_loop(board)


if __name__ == "__main__":
    main()
