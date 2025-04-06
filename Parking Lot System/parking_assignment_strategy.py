import heapq
from parking_spot import ParkingSpot

class ParkingAssignmentStrategy:
    def __init__(self):
        self.min_heap = []

    def add_spot(self, spot: ParkingSpot):
        heapq.heappush(self.min_heap, (spot.spot_id, spot))

    def assign_nearest_spot(self):
        while self.min_heap:
            _, spot = heapq.heappop(self.min_heap)
            if spot.is_available:
                spot.assign_spot()
                return spot
        raise Exception("No available spots")
