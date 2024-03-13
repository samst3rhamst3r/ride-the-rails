import pytest
from . import train_card as tc

def test_locomotive():
    locomotive = tc.TrainType("Locomotive")
    assert locomotive is tc.TrainType.LOCOMOTIVE