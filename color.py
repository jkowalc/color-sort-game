from colorama import Style


class Color:
    def __init__(self, value) -> None:
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.value == other.value
        else:
            return False

    def __str__(self):
        if self.value:
            return f'\u2502{self.value}\u2588\u2588{Style.RESET_ALL}\u2502'
        else:
            return '\u2502  \u2502'
