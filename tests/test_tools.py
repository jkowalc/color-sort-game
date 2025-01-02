from color_sort_game.tools import convert_tuple_list_to_dict


def test_convert_to_dict():
    list = [(1, 2), (1, 3), (2, 2)]
    assert convert_tuple_list_to_dict(list) == {1: [2, 3], 2: [2]}


def test_convert_to_dict_2():
    list = [("one", "two"), ("one", "three")]
    assert convert_tuple_list_to_dict(list) == {"one": ["two", "three"]}
