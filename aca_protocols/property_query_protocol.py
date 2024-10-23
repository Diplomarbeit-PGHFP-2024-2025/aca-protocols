from uagents import Model

class PropertyQueryRequest(Model):
    pass

class PropertyQueryResponse(Model):
    open_time_frames: list[(int, int)]
    geo_point: (float, float)
    cost_per_kwh: float
    charging_wattage: int
    green_energy: bool
    station_provider: str
    energy_provider: str