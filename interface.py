from ampule import pour
from game_board import GameBoard, WinEvent, NoMoveEvent
from tools import get_ampule_from_letter, get_poss_from_source_letter
from tools import convert_tuple_list_to_dict


def main_loop():
    pass


def level_loop(board: GameBoard):
    while True:
        try:
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


def get_player_decision(possibilities):
    print_possibilities_all(possibilities)
    choice = input("Choose one ('1' or 'a' or 'aa' syntax): ")
    if choice.isdigit():
        choice = int(choice) - 1
        if choice < len(possibilities):
            return possibilities[choice]
        else:
            limit = len(possibilities) - 1
            print(f"Choice must be between 1 and {limit}. Try again.")
            return get_player_decision(possibilities)
    elif choice.isalpha():
        choice = choice.upper()
        if len(choice) == 2:
            source_letter = choice[0]
            dest_letter = choice[1]
            return handle_other_variants(possibilities,
                                         source_letter, dest_letter)
        elif len(choice) == 1:
            source_letter = choice
            return handle_other_variants(possibilities, source_letter)
        else:
            print("Too many letters. Try again.")
            return get_player_decision(possibilities)
    else:
        print("Wrong syntax. Try again.")
        return get_player_decision(possibilities)


def handle_other_variants(possibilities, source_letter, dest_letter=None):
    poss_dict = convert_tuple_list_to_dict(possibilities)
    first_poss_letters = [key.symbol for key in poss_dict.keys()]
    if source_letter not in first_poss_letters:
        first_poss_letters_str = str(first_poss_letters)[1:-1]
        print(f"First choice must be in {first_poss_letters_str}")
        return get_player_decision(possibilities)
    poss_from_source = get_poss_from_source_letter(poss_dict, source_letter)
    poss_ampules, source = poss_from_source
    poss_letters = [str(amp) for amp in poss_ampules]
    if not dest_letter:
        dest = get_second_choice(poss_ampules)
        return source, dest
    if dest_letter in poss_letters:
        dest = get_ampule_from_letter(poss_ampules, dest_letter)
        return source, dest
    else:
        poss_letters_str = str(poss_letters)[1:-1]
        print(f"Second letter must be in {poss_letters_str}")
        dest = get_second_choice(poss_ampules)
        return source, dest


def get_second_choice(poss_ampules):
    if len(poss_ampules) == 1:
        return poss_ampules[0]
    print_possibilities_source(poss_ampules)
    choice = input("Choose destination ('1' or 'a' syntax): ")
    if choice.isdigit():
        choice = int(choice) - 1
        if choice < len(poss_ampules):
            return poss_ampules[choice]
        else:
            limit = len(poss_ampules) - 1
            print(f"Choice must be between 1 and {limit}. Try again.")
            return get_second_choice(poss_ampules)
    elif choice.isalpha():
        poss_letters = [str(amp) for amp in poss_ampules]
        choice = choice.upper()
        if choice in poss_letters:
            return get_ampule_from_letter(poss_ampules, choice)
        else:
            poss_letters_str = str(poss_letters)[1:-1]
            print(f"Destination must be in {poss_letters_str}")
            return get_second_choice(poss_ampules)
    else:
        print("Wrong syntax. Try again.")
        return get_second_choice(poss_ampules)



def print_possibilities_all(possibilities):
    print("Possible pours: ")
    poss_str = ""
    for i, possibility in enumerate(possibilities):
        source = str(possibility[0])
        dest = str(possibility[1])
        poss_str += f"{i+1}. {source} -> {dest}, "
    print(poss_str)


def print_possibilities_source(ampules):
    print("Possible destinations: ")
    poss_str = ""
    for amp in ampules:
        poss_str += f"{amp}, "
    print(poss_str)
