import pytest
from ampule import Ampule
from color import Color
from game_board import GameBoard, NoMoveEvent, WinEvent


def test_win_condition():
    ampules = [
        Ampule(colors=[
            Color("red"),
            Color("red"),
            Color("red")
        ]),
        Ampule(colors=[
            Color("blue"),
            Color("blue"),
            Color("blue")
        ]),
        Ampule(colors=[
            Color(),
            Color(),
            Color()
        ])
    ]
    board = GameBoard(ampules=ampules)
    with pytest.raises(WinEvent):
        board.check_win_condition()


def test_win_condition_fail():
    ampules = [
        Ampule(colors=[
            Color("red"),
            Color("red"),
            Color("blue")
        ]),
        Ampule(colors=[
            Color("blue"),
            Color("blue"),
            Color("red")
        ]),
        Ampule(colors=[
            Color(),
            Color(),
            Color()
        ])
    ]
    board = GameBoard(ampules=ampules)
    board.check_win_condition()


def test_win_condition_fail_two():
    ampules = [
        Ampule(colors=[
            Color("red"),
            Color("red"),
            Color("red")
        ]),
        Ampule(colors=[
            Color("blue"),
            Color("blue"),
            Color()
        ]),
        Ampule(colors=[
            Color("blue"),
            Color(),
            Color()
        ])
    ]
    board = GameBoard(ampules=ampules)
    board.check_win_condition()


def test_get_possible_pours():
    ampule1 = Ampule(colors=[
        Color("blue"),
        Color("red")
    ], max_height=3)
    ampule2 = Ampule(colors=[
        Color("red")
    ], max_height=3)
    board = GameBoard([ampule1, ampule2])
    assert board.get_possible_pours() == [(ampule1, ampule2), (ampule2, ampule1)]


def test_get_possible_pours_one():
    ampule1 = Ampule(colors=[
        Color("blue"),
        Color("red")
    ], max_height=2)
    ampule2 = Ampule(colors=[
        Color("red")
    ], max_height=2)
    board = GameBoard([ampule1, ampule2])
    assert board.get_possible_pours() == [(ampule1, ampule2)]


def test_get_possible_pours_nomove():
    ampule1 = Ampule(colors=[
        Color("red"),
        Color("blue")
    ], max_height=2)
    ampule2 = Ampule(colors=[
        Color("red")
    ], max_height=2)
    board = GameBoard([ampule1, ampule2])
    with pytest.raises(NoMoveEvent):
        board.get_possible_pours()
