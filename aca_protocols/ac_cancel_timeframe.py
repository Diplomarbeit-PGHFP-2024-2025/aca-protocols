from uagents import Model


class CancelTimeFrameReqeust(Model):
    sender_address: str
    timeframe: (float, float)


class CancelTimeFrameResponse(Model):
    pass
