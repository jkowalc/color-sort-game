from color_sort_game.tools import get_ampule_from_letter, get_poss_from_source_letter, convert_tuple_list_to_dict
from color_sort_game.config import config

CONFIG = config()


def get_player_decision(possibilities):
    if CONFIG["game_rules"]["print_all_possibilities"]:
        print_possibilities_all(possibilities)
        syntax = CONFIG["msg"]["syntax"]["double_letter"]
    else:
        syntax = CONFIG["msg"]["syntax"]["only_double_letter"]
    syntax_msg = syntax + " " + CONFIG["msg"]["syntax"]["word"]
    choice_msg = CONFIG["msg"]["choice"]["standard"]
    choice = input(f"{choice_msg} ({syntax_msg}): ")
    if choice.isdigit() and CONFIG["game_rules"]["print_all_possibilities"]:
        choice = int(choice) - 1
        limit = len(possibilities)
        if choice < limit:
            return possibilities[choice]
        else:
            print(CONFIG["msg"]["choice_outside_bounds"].format(limit))
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
            print(CONFIG["msg"]["too_many_letters"])
            return get_player_decision(possibilities)
    else:
        print(CONFIG["msg"]["wrong_syntax"].format(syntax))
        return get_player_decision(possibilities)


def handle_other_variants(possibilities, source_letter, dest_letter=None):
    poss_dict = convert_tuple_list_to_dict(possibilities)
    first_poss_letters = [key.symbol for key in poss_dict.keys()]
    if source_letter not in first_poss_letters:
        first_poss_letters_str = str(first_poss_letters)
        msg = CONFIG["msg"]["choice_must_be_in"]
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
        unformatted_msg = CONFIG["msg"]["choice_must_be_in"]
        print(unformatted_msg.format(poss_letters_str))
        dest = get_second_choice(poss_ampules)
        return source, dest


def get_second_choice(poss_ampules):
    if len(poss_ampules) == 1:
        return poss_ampules[0]
    if CONFIG["game_rules"]["print_source_possibilities"]:
        syntax = CONFIG["msg"]["syntax"]["single_letter"]
        print_possibilities_source(poss_ampules)
    else:
        syntax = CONFIG["msg"]["syntax"]["only_single_letter"]
    syntax_msg = syntax + " " + CONFIG["msg"]["syntax"]["word"]
    choice_msg = CONFIG["msg"]["choice"]["dest"]
    choice = input(f"{choice_msg} ({syntax_msg}): ")
    if choice.isdigit() and CONFIG["game_rules"]["print_source_possibilities"]:
        choice = int(choice) - 1
        limit = len(poss_ampules)
        if choice < limit:
            return poss_ampules[choice]
        else:
            print(CONFIG["msg"]["choice_outside_bounds"].format(limit))
            return get_second_choice(poss_ampules)
    elif choice.isalpha():
        poss_letters = [str(amp) for amp in poss_ampules]
        choice = choice.upper()
        if choice in poss_letters:
            return get_ampule_from_letter(poss_ampules, choice)
        else:
            poss_letters_str = str(poss_letters)
            msg = CONFIG["msg"]["choice_must_be_in"]
            print(msg.format(poss_letters_str))
            return get_second_choice(poss_ampules)
    else:
        print(CONFIG["msg"]["wrong_syntax"].format(syntax))
        return get_second_choice(poss_ampules)


def print_possibilities_all(possibilities):
    print(CONFIG["msg"]["possible_pours"])
    poss_str = ""
    for i, possibility in enumerate(possibilities):
        source = str(possibility[0])
        dest = str(possibility[1])
        poss_str += f"{i+1}. {source} -> {dest}, "
    print(poss_str)


def print_possibilities_source(ampules):
    print(CONFIG["msg"]["possible_destinations"])
    poss_str = ""
    for i, amp in enumerate(ampules):
        poss_str += f"{i+1}. {amp}, "
    print(poss_str)
