import pytest
from color_sort_game.game_logic.ampule import Ampule, AmpuleEmptyError, AmpuleFullError, pour
from color_sort_game.game_logic.color import Color


def test_get_top_color():
    colors = [
        Color("red")
    ]
    amp = Ampule("A", colors=colors)
    assert amp.get_top_color().value == "red"


def test_current_height():
    colors = [
        Color("red"),
        Color("blue"),
        Color("blue")
    ]
    amp = Ampule(colors=colors)
    assert amp.get_current_height() == 3
    assert amp.max_height == 3


def test_space_left():
    colors = [
        Color("red"),
        Color("blue"),
        Color("green")
    ]
    amp = Ampule(max_height=4, colors=colors)
    assert amp.get_space_left() == 1


def test_get_top_color_height_0():
    amp = Ampule()
    assert amp.get_top_color_height() == 0


def test_get_top_color_height_1():
    colors = [
        Color("red"),
        Color("blue"),
        Color("green")
    ]
    amp = Ampule(colors=colors)
    assert amp.get_top_color_height() == 1


def test_get_top_color_height_2():
    colors = [
        Color("red"),
        Color("blue"),
        Color("red"),
        Color("red")
    ]
    amp = Ampule(colors=colors)
    assert amp.get_top_color() == Color("red")
    assert amp.get_top_color_height() == 2


def test_get_top_color_height_monotone():
    colors = [
        Color("blue"),
        Color("blue")
    ]
    amp = Ampule(colors=colors)
    assert amp.get_top_color_height() == 2


def test_get_color_1():
    colors = [
        Color("red")
    ]
    amp = Ampule(colors=colors)
    assert amp.get_color(1).value is None
    assert amp.get_color(0).value == "red"


def test_get_color_2():
    amp = Ampule()
    assert amp.get_color(0).value is None
    assert amp.get_color(1).value is None


def test_add_color_on_top():
    colors = [
        Color("red")
    ]
    amp = Ampule(max_height=2, colors=colors)
    amp.add_color_on_top(Color("blue"), 1)
    assert amp.colors == [
        Color("red"),
        Color("blue")
    ]


def test_add_color_on_top_2():
    colors = [
        Color("red")
    ]
    amp = Ampule(max_height=3, colors=colors)
    amp.add_color_on_top(Color("blue"), 2)
    assert amp.colors == [
        Color("red"),
        Color("blue"),
        Color("blue")
    ]


def test_add_color_on_top_error():
    colors = [
        Color("red")
    ]
    amp = Ampule(max_height=2, colors=colors)
    with pytest.raises(AmpuleFullError):
        amp.add_color_on_top(Color("blue"), 2)


def test_remove_colors_from_top():
    colors = [
        Color("red"),
        Color("blue")
    ]
    amp = Ampule(colors=colors)
    amp.remove_colors_from_top(1)
    assert amp.colors == [
        Color("red")
    ]


def test_remove_colors_from_top_2():
    colors = [
        Color("red"),
        Color("blue")
    ]
    amp = Ampule(colors=colors)
    amp.remove_colors_from_top(2)
    assert amp.colors == []


def test_remove_colors_from_top_error():
    colors = [
        Color("red"),
        Color("blue")
    ]
    amp = Ampule(colors=colors)
    with pytest.raises(AmpuleEmptyError):
        amp.remove_colors_from_top(3)


def test_is_correct_empty():
    amp = Ampule()
    assert amp.is_correct()


def test_is_correct_empty_two():
    amp = Ampule(max_height=3)
    assert amp.is_correct()


def test_is_correct_full_incorrect():
    colors = [
        Color("blue"),
        Color("red"),
        Color("red")
    ]
    amp = Ampule(colors=colors)
    assert not amp.is_correct()


def test_is_correct_too_much_height():
    colors = [
        Color("red"),
        Color("red"),
        Color("red")
    ]
    amp = Ampule(max_height=4, colors=colors)
    assert not amp.is_correct()


def test_is_correct_full_correct():
    colors = [
        Color("red"),
        Color("red"),
        Color("red")
    ]
    amp = Ampule(colors=colors)
    assert amp.is_correct()


def test_pour():
    colors1 = [
        Color("red"),
        Color("blue"),
        Color("blue")
    ]
    colors2 = [
        Color("blue"),
        Color("blue")
    ]
    amp1 = Ampule("A", max_height=3, colors=colors1)
    amp2 = Ampule("B", max_height=3, colors=colors2)
    pour(amp1, amp2)
    assert amp1.colors == [
        Color("red"),
        Color("blue")
    ]
    assert amp2.colors == [
        Color("blue"),
        Color("blue"),
        Color("blue")
    ]


def test_pour_empty():
    colors1 = [
        Color("blue"),
        Color("blue")
    ]
    colors2 = [
        Color("blue")
    ]
    amp1 = Ampule(max_height=3, colors=colors1)
    amp2 = Ampule(max_height=3, colors=colors2)
    pour(amp1, amp2)
    assert amp1.colors == []
    assert amp2.colors == [
        Color("blue"),
        Color("blue"),
        Color("blue")
    ]
