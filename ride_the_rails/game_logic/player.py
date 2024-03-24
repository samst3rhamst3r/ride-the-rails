
from .train_card import TrainType

class Player:

    def __init__(self, name: str, train_cards: list, path_cards: list, train_pool: int) -> None:
        self.name = name
        self.train_cards = train_cards
        self.path_cards = path_cards
        self.train_pool = train_pool
    
    def add_path_cards(self, path_cards: list):
        self.path_cards.extend(path_cards)
    
    def add_train_cards(self, train_cards: list):
        self.train_cards.extend(train_cards)
    
    def rm_train_cards(self, train_type, num):
        
        indices = []
        for _ in range(num):
            for train_card_index, train_card in enumerate(self.train_cards):
                if train_card.type is train_type:
                    indices.append(train_card_index)
        
        for i, train_card_index in enumerate(indices):
            indices[i] = self.train_cards.pop(train_card_index)
        
        return tuple(indices)