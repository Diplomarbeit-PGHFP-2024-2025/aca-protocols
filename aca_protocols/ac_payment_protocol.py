from uagents import Model


class PaymentRequest(Model):
    wallet_address: str
    amount: int
    denomination: str

    # In blockchain, "denomination" refers to the unit of value
    # or currency in which transactions and balances are expressed.


class TransactionInfo(Model):
    transaction_hash: str


MIN_TEST_AMOUNT = 100
DENOM = "atestfet"  # Smallest unit of the Fetch.ai cryptocurrency "FET"
