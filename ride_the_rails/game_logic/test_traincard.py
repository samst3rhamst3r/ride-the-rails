import pytest
from .train_card import TrainCard, TrainType

class TestTrainType:

    def test_reg_train_type(self):
        t = TrainType("Box")
        assert t is TrainType.BOX
    
class TestTrainCard:

    def test_train_card_str_init(self):
        t = TrainCard("Locomotive")
        assert t.type is TrainType.LOCOMOTIVE
    
    def test_train_card_enum_init(self):
        t = TrainCard(TrainType.LOCOMOTIVE)
        assert t.type is TrainType.LOCOMOTIVE