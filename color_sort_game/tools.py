from collections import defaultdict

from color_sort_game.game_logic.ampule import Ampule
import os


def convert_tuple_list_to_dict(elements: list[tuple]) -> dict:
    result_dict = defaultdict(lambda: [])
    for element in elements:
        key, value = element
        result_dict[key].append(value)
    return dict(result_dict)


def get_ampule_from_letter(ampule_list: list[Ampule], letter) -> Ampule:
    for ampule in ampule_list:
        if ampule.symbol == letter:
            return ampule


def get_poss_from_source_letter(poss_dict: dict, source_letter: str):
    sources = poss_dict.keys()
    source = get_ampule_from_letter(sources, source_letter)
    return poss_dict[source], source


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
