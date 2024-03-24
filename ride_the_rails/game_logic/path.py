
import enum

class PathColor(enum.Enum):
    PINK = "Pink"
    WHITE = "White"
    BLUE = "Blue"
    YELLOW = "Yellow"
    ORANGE = "Orange"
    BLACK = "Black"
    RED = "Red"
    GREEN = "Green"
    GENERIC = None
    
class Path:

    def __init__(self, endpoints, length, colors, owners=None) -> None:
        self.endpoints = endpoints
        self.length = length
        self.colors = colors
        
        self.owners = [] if owners is None else owners
