class Color:
    def __init__(self, value) -> None:
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.value == other.value
        else:
            return False
