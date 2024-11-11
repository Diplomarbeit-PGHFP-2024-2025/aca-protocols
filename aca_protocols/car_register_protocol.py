from uagents import Model


class CarRegisterRequest(Model):
    # unix-timestamp when the timeframe starts
    start_time: float
    # duration of registration in seconds
    duration: float


class CarRegisterResponse(Model):
    # if the car was successfully registered
    success: bool
