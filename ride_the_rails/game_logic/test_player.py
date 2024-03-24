import pytest
from .player import Player
from .dest_card import DestCard
from .train_card import TrainCard

class TestPlayer:

    @pytest.fixture
    def player(self):
        return Player("test", [], [], 45)
    
    @pytest.fixture
    def path_card(self):
        return DestCard(['loc1', 'loc2'], 10)
    
    @pytest.fixture
    def train_card(self):
        return TrainCard("Box")

    def test_init(self, player):
        assert player.name == "test"
        assert len(player.path_cards) == 0
        assert len(player.train_cards) == 0
        assert player.train_pool == 45
    
    def test_add_path_card(self, player, path_card):
        player.add_path_cards([path_card])
        assert len(player.path_cards) == 1
    
    def test_fail_add_path_cards(self, player, path_card):
        with pytest.raises(TypeError):
            player.add_path_cards(path_card)
