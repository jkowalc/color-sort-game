from ampule import pour
from game_board import GameBoard, WinEvent, NoMoveEvent


def main_loop(board: GameBoard):
    while True:
        try:
            possibilites = board.get_possible_pours()
            print(board)
            player_choice = get_player_decision(possibilites)
            source, dest = player_choice
            pour(source, dest)
        except WinEvent:
            print("Win")
            break
        except NoMoveEvent:
            print("No move")
            break


def get_player_decision(possibilities):
    print("Possible pours: ")
    for i, possibility in enumerate(possibilities):
        source = str(possibility[0])
        dest = str(possibility[1])
        print(f"{i+1}. {source} -> {dest}")
    choice = int(input("Choose one: ")) - 1
    if choice < len(possibilities):
        return possibilities[choice]
    else:
        print("Wrong value.")
        return get_player_decision(possibilities)
