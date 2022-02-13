from ampule import Ampule, pour
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
