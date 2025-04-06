class MonitoringSystem:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def display_status(self):
        available_spots = len([spot for spot in self.parking_lot.spots if spot.is_available])
        print(f"Available Spots: {available_spots}/{self.parking_lot.capacity}")
