from uagents import Model


class StationRegisterRequest(Model):
    lat: float
    long: float


class StationRegisterResponse(Model):
    ttl: int  # Time to Live in seconds
