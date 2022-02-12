from __future__ import annotations
from typing import List
from color import Color


class Ampule:
    def __init__(self, max_height=None, colors=None):
        self.colors: List = colors if colors else None
        self.max_height = max_height if max_height else len(self.colors)

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
        if n <= self.get_current_height():
            return self.colors[n]
        else:
            return Color()

    def add_color(self, color, n):
        for i in range(n):
            self.colors.append(color)

    def remove_top_color(self, n):
        for i in range(n):
            self.colors.pop()


def can_be_poured(source: Ampule, dest: Ampule):
    if source.get_top_color() != dest.get_top_color():
        return False
    space_left = dest.get_space_left()
    return space_left > 0


def pour(source: Ampule, dest: Ampule):
    color = source.get_top_color()
    space_left = dest.get_space_left()
    max_quantity = source.get_top_color_height()
    actual_quantity = max(max_quantity, space_left)
    source.remove_top_color(actual_quantity)
    dest.add_color(color, actual_quantity)
