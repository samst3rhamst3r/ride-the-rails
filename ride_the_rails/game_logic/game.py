
import pathlib, json, random

from . import path
from .path_card import PathCard
from .train_card import TrainCard, TrainType
from .location import Location

class Game:

    @classmethod
    def New_Game(cls, num_players: int):

        d = None
        with open(pathlib.Path(__file__).parent / "data.json") as f:
            d = json.load(f)

        train_cards = []
        for train_dict in d["train_cards"]:
            
            train_type = TrainType(train_dict["name"])
            
            for _ in range(train_dict["cards_per_color"]):
                train_cards.append(TrainCard(train_type))
                
        random.shuffle(train_cards)

        path_cards = []
        for card_dict in d["path_cards"]:
            path_cards.append(PathCard(**card_dict))

        random.shuffle(path_cards)

        locations = {}
        paths = []
        for path_dict in d["paths"]:
            if start not in locations:
                locations[start] = Location(start)
            if end not in locations:
                locations[end] = Location(end)

    def __init__(self) -> None:
        pass