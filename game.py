from random import choice
from colorama import Fore
from ampule import Ampule

from color import Color
from game_board import GameBoard
COLORS = [
    Color(Fore.BLUE),
    Color(Fore.GREEN),
    Color(Fore.RED),
    Color(Fore.MAGENTA),
    Color(Fore.YELLOW),
    Color(Fore.CYAN)
]


class Game:
    def __init__(self, initial_board=None):
        if initial_board:
            self.board = initial_board

    def generate_board(self, max_height, empty_ampules, full_ampules):
        ampules = []
        colors = COLORS[:full_ampules]
        for _ in range(full_ampules):
            amp_colors = []
            for _ in range(max_height):
                color = choice(colors)
                amp_colors.append(color)
            ampules.append(Ampule(colors=amp_colors))
        for _ in range(empty_ampules):
            ampules.append(Ampule(max_height=max_height))
        self.board = GameBoard(ampules=ampules)


