from game_logic.ampule import pour
from game_logic.game_board import GameBoard, WinEvent, NoMoveEvent
from interface.player_decision import get_player_decision
from tools import clear_console


def main_loop():
    pass


def level_loop(board: GameBoard):
    while True:
        try:
            clear_console()
            possibilities = board.get_possible_pours()
            print(board)
            player_choice = get_player_decision(possibilities)
            source, dest = player_choice
            pour(source, dest)
        except WinEvent:
            print("Player won!")
            break
        except NoMoveEvent:
            print("Game over.")
            break
