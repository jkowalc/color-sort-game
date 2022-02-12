from ampule import pour
from game_board import GameBoard, WinEvent, NoMoveEvent
from generate_board import generate_board


def main_loop(board: GameBoard):
    while True:
        try:
            board.check_conditions()
            possibilites = board.get_possible_pours()
            print(board)
            player_choice = get_player_decision(possibilites)
            source, dest = player_choice
            pour(source, dest)
        except WinEvent:
            pass
        except NoMoveEvent:
            pass


def get_player_decision(possibilities):
    print("Possible pours: ")
    for i, possibility in enumerate(possibilities):
        source = str(possibility[0])
        dest = str(possibility[1])
        print(f"{i}. {source} -> {dest}")
    choice = int(input("Choose one: "))
    if choice < len(possibilities):
        return possibilities[choice]
    else:
        print("Wrong value.")
        return get_player_decision(possibilities)
