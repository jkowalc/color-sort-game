from __future__ import annotations
from typing import List
from color import Color


class Ampule:
    def __init__(self, symbol, max_height=None, colors=None):
        self.colors: List = colors if colors else []
        self.max_height = max_height if max_height else len(self.colors)
        self.symbol = symbol

    def get_top_color(self):
        return self.colors[-1]

    def get_current_height(self):
        return len(self.colors)

    def get_space_left(self):
        return self.max_height - self.get_current_height()

    def get_top_color_height(self):
        top_color = self.get_top_color()
        top_color_height = 0
        amp_height = self.get_current_height()
        for color_i in range(-1, -amp_height, -1):
            if self.colors[color_i] == top_color:
                top_color_height += 1
            else:
                return top_color_height
        return top_color_height

    def get_color(self, n):
        if n <= self.get_current_height()-1:
            return self.colors[n]
        else:
            return Color()

    def add_color_on_top(self, color, n):
        for _ in range(n):
            self.colors.append(color)

    def remove_top_color(self, n):
        for _ in range(n):
            self.colors.pop()

    def __str__(self):
        return self.symbol

    def is_correct(self):
        if self.get_current_height() == 0:
            return True
        if self.get_current_height() != self.max_height:
            return False
        top_color = self.get_top_color()
        for color in self.colors:
            if color != top_color:
                return False
        return True


def can_be_poured(source: Ampule, dest: Ampule):
    if dest.get_current_height() == 0 and source.get_current_height() > 0:
        return True
    if source.get_current_height() == 0:
        return False
    if source.get_top_color() != dest.get_top_color():
        return False
    space_left = dest.get_space_left()
    return space_left > 0


def pour(source: Ampule, dest: Ampule):
    color = source.get_top_color()
    space_left = dest.get_space_left()
    max_quantity = source.get_top_color_height()
    actual_quantity = min(max_quantity, space_left)
    source.remove_top_color(actual_quantity)
    dest.add_color_on_top(color, actual_quantity)
