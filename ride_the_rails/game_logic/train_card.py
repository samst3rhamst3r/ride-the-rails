import enum
from .path import PathColor

class TrainType(enum.Enum):
    BOX = "Box"
    PASSENGER = "Passenger"
    TANKER = "Tanker"
    REEFER = "Reefer"
    FREIGHT = "Freight"
    HOPPER = "Hopper"
    COAL = "Coal"
    CABOOSE = "Caboose"
    LOCOMOTIVE = "Locomotive"

class TrainCard:

    _train_path_map = {
        TrainType.BOX: PathColor.PINK,
        TrainType.PASSENGER: PathColor.WHITE,
        TrainType.TANKER: PathColor.BLUE,
        TrainType.REEFER: PathColor.YELLOW,
        TrainType.FREIGHT: PathColor.ORANGE,
        TrainType.HOPPER: PathColor.BLACK,
        TrainType.COAL: PathColor.RED,
        TrainType.CABOOSE: PathColor.GREEN,
        TrainType.LOCOMOTIVE: None
    }

    def __init__(self, type: TrainType | str) -> None:
        self.type = TrainType(type)
