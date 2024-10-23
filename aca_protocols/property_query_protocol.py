from uagents import Model


class PropertyQueryRequest(Model):
    pass


class PropertyQueryResponse(Model):
    # The first value in the tuple represents the seconds since 1970 when the timeframe starts
    # The second value in the tuple represents the seconds since 1970 when the timeframe ends
    open_time_frames: list[(int, int)]
    # Representing long and lat of the station
    geo_point: (float, float)
    cost_per_kwh: float
    charging_wattage: int
    green_energy: bool
    station_provider_name: str
    energy_provider_name: str
