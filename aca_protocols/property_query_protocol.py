from typing import Tuple

from uagents import Model


class PropertyQueryRequest(Model):
    pass


class PropertyQueryResponse(Model):
    # First value: unix-timestamp when the timeframe starts
    # Second value: unix-timestamp when the timeframe ends
    open_time_frames: list[(int, int)]
    # Representing long and lat of the station
    geo_point: Tuple[float, float]
    cost_per_kwh: float
    charging_wattage: int
    green_energy: bool
