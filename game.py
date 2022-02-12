from random import choice
from colorama import Fore
from ampule import Ampule

from color import Color
from game_board import GameBoard
COLORS = [
    Fore.BLUE,
    Fore.GREEN,
    Fore.RED,
    Fore.MAGENTA,
    Fore.YELLOW,
    Fore.CYAN
]


class Game:
    def __init__(self, initial_board=None):
        if initial_board:
            self.board = initial_board

    def generate_board(self, max_height, full_ampules, empty_ampules):
        ampules = []
        colors = COLORS[:full_ampules]
        color_uses = {color: 0 for color in colors}
        for _ in range(full_ampules):
            amp_colors = []
            for _ in range(max_height):
                available_colors = [color for color in colors if color_uses[color]<max_height]
                color = choice(available_colors)
                color_uses[color] += 1
                amp_colors.append(Color(color))
            ampules.append(Ampule(colors=amp_colors))
        for _ in range(empty_ampules):
            ampules.append(Ampule(max_height=max_height))
        self.board = GameBoard(ampules=ampules)


