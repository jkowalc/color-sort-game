from dataclasses import dataclass
from colorama import Style

from color_sort_game.color_translation import text_to_code


@dataclass
class Color:
    value: str = None

    def __str__(self):
        if self.value:
            color_code = text_to_code(self.value)
            return f'\u2502{color_code}\u2588\u2588{Style.RESET_ALL}\u2502'
        else:
            return '\u2502  \u2502'
