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

    # Hashable: Implementing __hash__ and __eq__
    def __hash__(self):
        # Create a hash based on immutable attributes
        return hash(
            (
                tuple(
                    self.open_time_frames
                ),  # Convert list to tuple to make it hashable
                self.geo_point,
                self.cost_per_kwh,
                self.charging_wattage,
                self.green_energy,
            )
        )

    def __eq__(self, other):
        if not isinstance(other, PropertyData):
            return False
        return (
            self.open_time_frames == other.open_time_frames
            and self.geo_point == other.geo_point
            and self.cost_per_kwh == other.cost_per_kwh
            and self.charging_wattage == other.charging_wattage
            and self.green_energy == other.green_energy
        )


class PropertyCarData(Model):
    green_energy: bool
    cost_per_kwh: float
    charging_wattage: int

    max_km: int
    time_frames: list[Tuple[int, int]]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def from_json(data: str):
        return json.loads(data, object_hook=lambda d: PropertyData(**d))


class PropertyQueryRequest(Model):
    pass


class PropertyQueryResponse(Model):
    properties: str  # is the json representation of an object of PropertyData (expected return of to_json)
