from ampule import Ampule
from color import Color


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
