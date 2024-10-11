from uagents import Model


class StationQueryRequest(Model):
    lat: float
    long: float
    radius: float


class StationQueryResponse(Model):
    stations: list[str]
