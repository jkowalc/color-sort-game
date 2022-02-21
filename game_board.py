from itertools import permutations
from typing import List
from ampule import Ampule, can_be_poured


class WinEvent(Exception):
    pass


class NoMoveEvent(Exception):
    pass


class GameBoard:
    def __init__(self, ampules: List[Ampule] = None, title=None):
        self.ampules = ampules if ampules else []
        self.max_height = ampules[0].max_height if ampules else 0
        self.title = title

    def get_ampules_num(self):
        return len(self.ampules)

    def check_win_condition(self):
        is_satisfied = True
        for ampule in self.ampules:
            if not ampule.is_correct():
                is_satisfied = False
        if is_satisfied:
            raise WinEvent

    def get_possible_pours(self):
        self.check_win_condition()
        possibilites = permutations(self.ampules, 2)
        possible_pours = []
        for possibility in possibilites:
            source = possibility[0]
            dest = possibility[1]
            if can_be_poured(source, dest):
                possible_pours.append(possibility)
        if len(possible_pours) == 0:
            raise NoMoveEvent
        return possible_pours

    def __str__(self):
        board_str = ""
        for i in range(self.max_height - 1, -1, -1):
            for amp in self.ampules:
                board_str += str(amp.get_color(i))
                board_str += ' '
            board_str += "\n"
        for amp in self.ampules:
            board_str += "\u2570\u2500\u2500\u256F "
        board_str += "\n"
        for amp in self.ampules:
            board_str += f" {amp}   "
        board_str += "\n"
        return board_str
