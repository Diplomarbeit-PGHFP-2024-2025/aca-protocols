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

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def from_json(data: str):
        return json.loads(data, object_hook=lambda d: PropertyData(**d))


class PropertyCarData(Model):
    green_energy: bool
    cost_per_kwh: float
    charging_wattage: int

    max_km: int
    time_frames: list[(int, int)]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def from_json(data: str):
        return json.loads(data, object_hook=lambda d: PropertyData(**d))


class PropertyQueryRequest(Model):
    pass


class PropertyQueryResponse(Model):
    properties: str  # is the json representation of an object of PropertyData (expected return of to_json)
