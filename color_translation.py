from colorama import Fore

COLORS = {
    "blue": Fore.BLUE,
    "green": Fore.GREEN,
    "red": Fore.RED,
    "magenta": Fore.MAGENTA,
    "yellow": Fore.YELLOW,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
    "black": Fore.BLACK
}


def text_to_code(text):
    if text not in COLORS.keys():
        return None
    return COLORS[text]


def get_possible_colors():
    return COLORS.keys()
