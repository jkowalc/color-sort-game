from typing import List, Tuple
from ampule import Ampule


def convert_tuple_list_to_dict(list: List[Tuple]) -> dict:
    result_dict = {}
    for element in list:
        key, value = element
        if key not in result_dict.keys():
            result_dict[key] = []
        result_dict[key].append(value)
    return result_dict


def get_ampule_from_letter(ampule_list: List[Ampule], letter) -> Ampule:
    for ampule in ampule_list:
        if ampule.symbol == letter:
            return ampule


def get_poss_from_source_letter(poss_dict: dict, source_letter: str):
    sources = poss_dict.keys()
    source = get_ampule_from_letter(sources, source_letter)
    return poss_dict[source], source
