class TariffCalculator:
    def __init__(self, hourly_rate: float):
        self.hourly_rate = hourly_rate

    def calculate_fee(self, hours: int):
        return hours * self.hourly_rate
