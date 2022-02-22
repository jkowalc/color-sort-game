import config
from interface.level_loop import level_loop
from save_load_gameboard import load_game_board_from_json

def main_menu():
    print("Main menu\n")
    print("1. Choose level")
    print("2. Generate custom board")
    choice = input(config.CONFIG["standard_choice_msg"])
    if choice == "1":
        level = choose_level()
        if not level:
            main_menu()
        with open(f"levels/level_{level}") as fp:
            board = load_game_board_from_json(fp)
        level_loop(board)
    elif choice == "2":
        board_conf = get_board_conf()


def choose_level():
    print(f"Currently implemented levels: 1-{config.CONFIG['max_level']}")
    choice = input(config.CONFIG["standard_choice_msg"])
    if choice == "\q":
        return None
    if not choice.isdigit():
        print(config.CONFIG["wrong_syntax_msg"])
        return choose_level()
    choice = int(choice)
    if not 1 <= choice <= config.CONFIG["max_level"]:
        print()


def get_board_conf():
    pass