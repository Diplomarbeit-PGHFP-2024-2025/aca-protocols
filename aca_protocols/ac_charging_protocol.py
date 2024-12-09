from uagents import Model


class CarStartedChargingInfo(Model):
    pass


class CarFinishedChargingInfo(Model):
    kwh_charged: float
