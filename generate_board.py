from random import choice
from ampule import Ampule
from color import Color
from game_board import GameBoard
from colorama import Fore
COLORS = [
    Fore.BLUE,
    Fore.GREEN,
    Fore.RED,
    Fore.MAGENTA,
    Fore.YELLOW,
    Fore.CYAN
]

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_board(max_height, full_ampules, empty_ampules):
    ampules = []
    colors = COLORS[:full_ampules]
    symbols = list(SYMBOLS)
    color_uses = {color: 0 for color in colors}
    for _ in range(full_ampules):
        amp_colors = []
        for _ in range(max_height):
            available_colors = [
                color for color in colors
                if color_uses[color] < max_height
            ]
            color = choice(available_colors)
            color_uses[color] += 1
            amp_colors.append(Color(color))
        ampules.append(Ampule(symbol=symbols[0], colors=amp_colors))
        symbols.pop(0)
    for _ in range(empty_ampules):
        ampules.append(Ampule(symbol=symbols[0], max_height=max_height))
        symbols.pop(0)
    return GameBoard(ampules=ampules)
