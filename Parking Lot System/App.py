from parking_lot import ParkingLot
from parking_spot import ParkingSpot, ParkingSpotType
from parking_assignment_strategy import ParkingAssignmentStrategy
from monitoring_system import MonitoringSystem
from payment_strategy import CardPayment
from terminal import EntryTerminal, ExitTerminal

def main():
    # Initialize Parking Lot
    parking_lot = ParkingLot(capacity=2000)
    assignment_strategy = ParkingAssignmentStrategy()
    monitoring_system = MonitoringSystem(parking_lot)

    # Add parking spots
    for i in range(1, 501):
        spot = ParkingSpot(i, ParkingSpotType.HANDICAP)
        parking_lot.add_parking_spot(spot)
        assignment_strategy.add_spot(spot)

    for i in range(501, 1501):
        spot = ParkingSpot(i, ParkingSpotType.COMPACT)
        parking_lot.add_parking_spot(spot)
        assignment_strategy.add_spot(spot)

    for i in range(1501, 2001):
        spot = ParkingSpot(i, ParkingSpotType.LARGE)
        parking_lot.add_parking_spot(spot)
        assignment_strategy.add_spot(spot)

    # Display initial status
    monitoring_system.display_status()

    # Simulate entry
    entry_terminal = parking_lot.entry_terminals[0]
    assigned_spot = assignment_strategy.assign_nearest_spot()
    ticket = entry_terminal.issue_ticket(assigned_spot.spot_id, assigned_spot.spot_type)
    print(f"Ticket issued for Spot ID: {ticket.spot_id}, Spot Type: {assigned_spot.spot_type.name}")

    # Simulate exit
    exit_terminal = parking_lot.exit_terminals[0]
    payment_strategy = CardPayment()
    exit_terminal.process_payment(ticket, payment_strategy)

    # Display final status
    monitoring_system.display_status()

if __name__ == "__main__":
    main()
