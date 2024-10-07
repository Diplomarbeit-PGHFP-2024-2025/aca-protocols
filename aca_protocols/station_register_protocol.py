from uagents import Protocol, Model


class StationRegisterRequest(Model):
    lat: float
    long: float


class StationRegisterResponse(Model):
    pass


protocol = Protocol()
