from parking_spot import ParkingSpot, ParkingSpotType
from terminal import EntryTerminal, ExitTerminal

class ParkingLot:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.spots = []
        self.entry_terminals = [EntryTerminal(i) for i in range(4)]
        self.exit_terminals = [ExitTerminal(i) for i in range(4)]

    def add_parking_spot(self, spot: ParkingSpot):
        if len(self.spots) < self.capacity:
            self.spots.append(spot)
        else:
            raise Exception("Parking Lot is full")

    def get_available_spots(self, spot_type: ParkingSpotType):
        return [spot for spot in self.spots if spot.spot_type == spot_type and spot.is_available]
