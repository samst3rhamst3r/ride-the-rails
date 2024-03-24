import pytest
from .game import Game
from .player import Player

class TestGame:

    @pytest.fixture
    def players(self):
        p = []
        p.append(Player("human", [], [], 45))
        for i in range(4):
            p.append(Player(f"comp{i + 1}", [], [], 45))
        return p

    @pytest.fixture
    def new_game(self, players):
        return Game.New_Game(players)

    def test_newgame(self, new_game):
        assert len(new_game.players) == 5