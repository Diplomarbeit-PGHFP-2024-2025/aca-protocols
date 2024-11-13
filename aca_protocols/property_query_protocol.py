from typing import Tuple
import json
from uagents import Model


class PropertyData:
    def __init__(
        self, open_time_frames, geo_point, cost_per_kwh, charging_wattage, green_energy
    ):
        self.open_time_frames = open_time_frames
        self.geo_point = geo_point
        self.cost_per_kwh = cost_per_kwh
        self.charging_wattage = charging_wattage
        self.green_energy = green_energy

    # First value: unix-timestamp when the timeframe starts
    # Second value: unix-timestamp when the timeframe ends
    open_time_frames: list[Tuple[int, int]]
    # Representing long and lat of the station
    geo_point: Tuple[float, float]
    cost_per_kwh: float
    charging_wattage: int
    green_energy: bool

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def fromJson(data: str):
        return json.loads(data, object_hook=lambda d: PropertyData(**d))


class PropertyQueryRequest(Model):
    pass


class PropertyQueryResponse(Model):
    properties: PropertyData
