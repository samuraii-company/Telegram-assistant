from typing import Protocol
from config import Config
from binance.client import Client


class Currency(Protocol):
    """
    Abstract class Currency
    """
    def check_tokens(self):
        ...

    def prices(self):
        ...


class Crypto:
    """
    Crypto Currency
    """
    _token_list = ["BTC", "ETH", "ADA", "XRP"]

    def __init__(self):
        self.client = Client(Config.api_key, Config.api_secret)
        self.arr: list = []
        self.check_tokens()

    def check_tokens(self) -> None:
        """
        Check data from Binance API
        """
        for x in Crypto._token_list:
            price = self.client.get_symbol_ticker(symbol=f"{x}USDT")['price']
            self.arr.append({
                "token": x,
                "price": price
            })

    @property
    def prices(self) -> list[str, str]:
        """
        Get Tokens Price
        """
        return self.arr


class USD:
    """
    Real Currency USD
    """
    def __init__(self):
        self.client = Client(Config.api_key, Config.api_secret)
        self.check_tokens()

    def check_tokens(self) -> None:
        """
        Check data from Binance API
        """
        self.price = self.client.get_symbol_ticker(symbol="USDTRUB")['price']

    @property
    def prices(self) -> list[str, str]:
        """
        Get USDT/RUB Price
        """
        return {
            "token": "USDT",
            "price": self.price
        }
