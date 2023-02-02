class Trader:
    def __init__(self):
        # Add any additional info you want
        pass

    def MakeTrades(self, time, stock_prices):
        """
        Grader will call this once per timestep to determine your buys/sells.
        Args:
            time: int
            stock_prices: dict[string -> float]
        Returns:
            trades: dict[string -> float] of your trades (quantity) for this timestep.
                Positive is buy/long and negative is sell/short.
        """
        trades = {}
        return trades


class BullishTrader(Trader):
    def MakeTrades(self, time, stock_prices):
        return {"Stock1": 1000000, "Stock2": 1000000, "Stock3": 1000000, "Stock4": 1000000}


class BearishTrader(Trader):
    def MakeTrades(self, time, stock_prices):
        return {"Stock1": -1000000, "Stock2": -1000000, "Stock3": -1000000, "Stock4": -1000000}


class SampleTrader(Trader):
    def MakeTrades(self, time, stock_prices):
        trades = {}
        # TODO: PICK HOW TO MAKE TRADES.
        trades['Stock1'] = 1000
        if 'Stock2' in stock_prices:
            if stock_prices['Stock2'] > 123:
                trades['Stock2'] = 1000
            else:
                trades['Stock2'] = -1000
        return trades
