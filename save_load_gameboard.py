import json
from ampule import Ampule
from color import Color
from game_board import GameBoard


def save_game_board_to_json(fp, board: GameBoard):
    data = {"title": board.title, "max_height": board.max_height}
    for amp in board.ampules:
        data[amp.symbol] = [
            color.value for color in amp.colors
        ]
    json.dump(data, fp, indent=4)


def load_game_board_from_json(fp) -> GameBoard:
    data: dict = json.load(fp)
    ampules = []
    for key, item in data.items():
        if key == "title":
            title = item
            continue
        if key == "max_height":
            max_height = item
            continue
        colors = [
            Color(color) for color in item
        ]
        amp = Ampule(symbol=key, max_height=max_height, colors=colors)
        ampules.append(amp)
    board = GameBoard(ampules, title)
    return board
