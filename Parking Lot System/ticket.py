from datetime import datetime
from parking_spot import ParkingSpotType

class Ticket:
    def __init__(self, spot_id: int, spot_type: ParkingSpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.issue_time = datetime.now()
        self.is_paid = False

    def calculate_fee(self):
        current_time = datetime.now()
        hours_parked = (current_time - self.issue_time).seconds // 3600
        if hours_parked == 0:  # Minimum charge for the first hour
            hours_parked = 1

        if self.spot_type == ParkingSpotType.COMPACT or self.spot_type == ParkingSpotType.LARGE:
            return hours_parked * 30
        elif self.spot_type == ParkingSpotType.TWO_WHEELER:
            return hours_parked * 20
        elif self.spot_type == ParkingSpotType.HANDICAP:
            return hours_parked * 10
        else:
            raise ValueError("Invalid Parking Spot Type")

    def mark_paid(self):
        self.is_paid = True
