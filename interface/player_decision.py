from tools import get_ampule_from_letter, get_poss_from_source_letter
from tools import convert_tuple_list_to_dict
import config


def get_player_decision(possibilities):
    if config.PrintAllPossibilitiesRule:
        print_possibilities_all(possibilities)
    choice = input(config.CONFIG["msg"]["player_decision"])
    if choice.isdigit():
        choice = int(choice) - 1
        limit = len(possibilities)
        if choice < limit:
            return possibilities[choice]
        else:
            print(config.CONFIG["msg"]["choice_outside_bounds"].format(limit))
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
            print(config.CONFIG["msg"]["too_many_letters"])
            return get_player_decision(possibilities)
    else:
        print(config.CONFIG["msg"]["wrong_syntax"])
        return get_player_decision(possibilities)


def handle_other_variants(possibilities, source_letter, dest_letter=None):
    poss_dict = convert_tuple_list_to_dict(possibilities)
    first_poss_letters = [key.symbol for key in poss_dict.keys()]
    if source_letter not in first_poss_letters:
        first_poss_letters_str = str(first_poss_letters)
        msg = config.CONFIG["msg"]["choice_must_be_in"]
        print(msg.format(first_poss_letters_str))
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
        poss_letters_str = str(poss_letters)
        unformatted_msg = config.CONFIG["msg"]["choice_must_be_in"]
        print(unformatted_msg.format(poss_letters_str))
        dest = get_second_choice(poss_ampules)
        return source, dest


def get_second_choice(poss_ampules):
    if len(poss_ampules) == 1:
        return poss_ampules[0]
    if config.PrintSourcePossibilitiesRule:
        print_possibilities_source(poss_ampules)
    choice = input(config.CONFIG["msg"]["player_decision_dest"])
    if choice.isdigit():
        choice = int(choice) - 1
        limit = len(poss_ampules)
        if choice < limit:
            return poss_ampules[choice]
        else:
            print(config.CONFIG["msg"]["choice_outside_bounds"].format(limit))
            return get_second_choice(poss_ampules)
    elif choice.isalpha():
        poss_letters = [str(amp) for amp in poss_ampules]
        choice = choice.upper()
        if choice in poss_letters:
            return get_ampule_from_letter(poss_ampules, choice)
        else:
            poss_letters_str = str(poss_letters)
            msg = config.CONFIG["msg"]["choice_must_be_in"]
            print(msg.format(poss_letters_str))
            return get_second_choice(poss_ampules)
    else:
        print(config.CONFIG["msg"]["wrong_syntax"])
        return get_second_choice(poss_ampules)


def print_possibilities_all(possibilities):
    print(config.CONFIG["msg"]["possible_pours"])
    poss_str = ""
    for i, possibility in enumerate(possibilities):
        source = str(possibility[0])
        dest = str(possibility[1])
        poss_str += f"{i+1}. {source} -> {dest}, "
    print(poss_str)


def print_possibilities_source(ampules):
    print(config.CONFIG["msg"]["possible_destinations"])
    poss_str = ""
    for i, amp in enumerate(ampules):
        poss_str += f"{i+1}. {amp}, "
    print(poss_str)
