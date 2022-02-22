from generate_board import generate_board
import interface.level_loop as level_loop
from config import init_config


def main():
    init_config()
    board = generate_board(3, 2, 2)
    level_loop.level_loop(board)


if __name__ == "__main__":
    main()
