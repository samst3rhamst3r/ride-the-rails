
import pathlib, json, random

from .path import Path
from .dest_card import DestCard
from .train_card import TrainCard, TrainType

class Game:

    @classmethod
    def New_Game(cls, players):

        d = None
        with open(pathlib.Path(__file__).parent / "data.json") as f:
            d = json.load(f)

        train_cards = []
        for train_dict in d["train_cards"]:
            
            train_type = TrainType(train_dict["name"])
            
            for _ in range(train_dict["cards_per_color"]):
                train_cards.append(TrainCard(train_type))
                
        random.shuffle(train_cards)

        dest_cards = []
        for card_dict in d["dest_cards"]:
            dest_cards.append(DestCard(**card_dict))

        random.shuffle(dest_cards)

        location_paths = {}
        for path_dict in d["paths"]:
            path = Path(**path_dict)
            for endpoint in path.endpoints:
                if endpoint not in location_paths:
                    location_paths[endpoint] = []
                location_paths[endpoint].append(path)
        
        return cls(players, location_paths, train_cards, dest_cards)

    def __init__(self, players, location_paths, train_card_deck, dest_card_deck, 
                 face_up_dest_cards=None, 
                 train_discard_pile=None, 
                 dest_discard_pile=None) -> None:
        
        self.players = players
        self.loc_paths = location_paths
        self.train_deck = train_card_deck
        self.dest_deck = dest_card_deck

        self.face_up_dest_deck = face_up_dest_cards
        self.train_discard_pile = train_discard_pile
        self.dest_discard_pile = dest_discard_pile

        if face_up_dest_cards is None:
            self.face_up_dest_deck = [self.dest_deck.pop() for _ in range(5)]
        
        if train_discard_pile is None:
            self.train_discard_pile = []

        if dest_discard_pile is None:
            self.dest_discard_pile = []