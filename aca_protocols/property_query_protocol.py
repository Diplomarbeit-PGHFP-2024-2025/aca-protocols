from typing import Tuple
import json
from uagents import Model

class PropertyData(Model):
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
    properties: object
