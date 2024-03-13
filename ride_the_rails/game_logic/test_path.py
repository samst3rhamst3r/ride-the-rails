import pytest
from .path import Path, PathColor

class TestPathColor:

    def test_reg_color(self):
        path_color = PathColor("Green")
        assert path_color is PathColor.GREEN
    
    def test_generic(self):
        path_color = PathColor(None)
        assert path_color is PathColor.GENERIC

