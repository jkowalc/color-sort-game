from color_sort_game.config import config
from color_sort_game.game_logic.ampule import pour
from color_sort_game.game_logic.game_board import GameBoard, WinEvent, NoMoveEvent
from color_sort_game.interface.player_decision import get_player_decision
from color_sort_game.tools import clear_console

CONFIG = config()


def level_loop(board: GameBoard, win_func, fail_func):
    while True:
        try:
            clear_console()
            possibilities = board.get_possible_pours()
            print(board)
            player_choice = get_player_decision(possibilities)
            source, dest = player_choice
            pour(source, dest)
        except WinEvent:
            print(CONFIG["msg"]["win"])
            win_func()
            break
        except NoMoveEvent:
            print(CONFIG["msg"]["fail"])
            fail_func()
            break
