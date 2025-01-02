from typing import Tuple
from color_sort_game.config import config
from color_sort_game.generate_board import generate_board
from color_sort_game.interface.level_loop import level_loop
from color_sort_game.save_load_gameboard import load_game_board_from_json

CONFIG = config()


def main_menu():
    print(CONFIG["msg"]["welcome"])
    msg = (CONFIG['msg']['choice']['standard']
           + " ("
           + CONFIG['msg']['syntax']['num'] + " "
           + CONFIG['msg']['syntax']['word'] + "): ")
    choice = input(msg)
    if choice == "1":
        level = choose_level()
        with open(CONFIG['levels']['folder']
                  + CONFIG['levels']['file_format'].format(level)) as fp:
            board = load_game_board_from_json(fp)
        level_loop(board, main_menu, main_menu)
    elif choice == "2":
        board_conf = get_board_conf()
        board = generate_board(*board_conf)
        level_loop(board, main_menu, main_menu)
    else:
        print(CONFIG["msg"]["choice_outside_bounds"].format(2))
        main_menu()


def choose_level():
    max_level = CONFIG["levels"]["max_level"]
    print(CONFIG["msg"]["currently_implemented"].format(max_level))
    syntax = CONFIG["msg"]['syntax']["num"]
    syntax_msg = syntax + " " + CONFIG["msg"]["syntax"]['word']
    choice_msg = CONFIG["msg"]["choice"]["standard"]
    choice = input(f"{choice_msg} ({syntax_msg}): ")
    if choice == "\\q":
        main_menu()
    if not choice.isdigit():
        print(CONFIG["msg"]["wrong_syntax"].format(syntax))
        return choose_level()
    choice = int(choice)
    if not 1 <= choice <= max_level:
        print(CONFIG["msg"]["choice_outside_bounds"].format(max_level))
        return choose_level()
    return choice


def get_board_conf() -> Tuple[int, int, int]:
    print(CONFIG["msg"]['choice']["board_conf"] + "\n")
    max_height = input(CONFIG["msg"]['choice']["amp_height"] + ": ")
    full_ampules = input(CONFIG["msg"]['choice']["num_full_amp"] + ": ")
    empty_ampules = input(CONFIG["msg"]['choice']["num_empty_amp"] + ": ")
    if not (max_height.isdigit() and
            full_ampules.isdigit() and
            empty_ampules.isdigit()):
        print(CONFIG["msg"]["all_must_be_numbers"])
        return get_board_conf()
    return int(max_height), int(full_ampules), int(empty_ampules)
