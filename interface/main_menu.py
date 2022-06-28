from typing import Tuple
import config
from generate_board import generate_board
from interface.level_loop import level_loop
from save_load_gameboard import load_game_board_from_json


def main_menu():
    print("Main menu\n")
    print("1. Choose level")
    print("2. Generate custom board")
    choice = input(config.CONFIG["msg"]["standard_choice"])
    if choice == "1":
        level = choose_level()
        with open(f"levels/level_{level}.json") as fp:
            board = load_game_board_from_json(fp)
        level_loop(board, main_menu, main_menu)
    elif choice == "2":
        board_conf = get_board_conf()
        board = generate_board(board_conf[0], board_conf[1], board_conf[2])
        level_loop(board, main_menu, main_menu)
    else:
        print("Wrong value")
        main_menu()


def choose_level():
    print(f"Currently implemented levels: 1-{config.CONFIG['max_level']}")
    choice = input(config.CONFIG["msg"]["standard_choice"])
    if choice == "\\q":
        main_menu()
    if not choice.isdigit():
        print(config.CONFIG["msg"]["wrong_syntax"])
        return choose_level()
    choice = int(choice)
    if not 1 <= choice <= config.CONFIG["max_level"]:
        print("Wrong value")
        return choose_level()
    return choice


def get_board_conf() -> Tuple[int, int, int]:
    print("Choose board configuration")
    max_height = input("Choose ampule height: ")
    full_ampules = input("Choose number of full ampules: ")
    empty_ampules = input("Choose number of empty ampules: ")
    if not (max_height.isdigit() and
            full_ampules.isdigit() and
            empty_ampules.isdigit()):
        print("All values must be numbers")
        return get_board_conf()
    return int(max_height), int(full_ampules), int(empty_ampules)
