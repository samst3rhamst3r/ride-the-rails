
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

    def __init__(self, loc1, loc2, length, colors, owners=None) -> None:
        self.loc1 = loc1
        self.loc2 = loc2
        self.length = length
        self.colors = colors
        
        self.owners = [] if owners is None else owners

    