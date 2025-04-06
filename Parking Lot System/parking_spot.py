from enum import Enum

class ParkingSpotType(Enum):
    HANDICAP = "Handicap"
    COMPACT = "Compact"
    LARGE = "Large"
    TWO_WHEELER = "2Wheeler"

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: ParkingSpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_available = True

    def assign_spot(self):
        self.is_available = False

    def free_spot(self):
        self.is_available = True
