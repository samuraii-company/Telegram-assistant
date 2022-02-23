from typing import Protocol

from config import Config, wake_up_message
from currency import Currency
from weather import Weather
import telebot


class AbstractWorker(Protocol):
    def send_message(self):
        ...


class Worker:
    def __init__(self, currency: Currency, crypto: Currency):
        self.admin_id = Config.admin_id
        self.crypto = crypto()
        self.currency = currency()
        self.weather = Weather("Kirov")
        self.bot = telebot.TeleBot(Config.token, parse_mode=None)

    def send_message(self):
        """
        Function send message
        about crypto curency and real currency
        """
        self.bot.send_message(
            chat_id=self.admin_id,
            text=wake_up_message.format(
                btc=self.crypto.prices[0]["price"],
                eth=self.crypto.prices[1]["price"],
                ada=self.crypto.prices[2]["price"],
                xrp=self.crypto.prices[3]["price"],
                usd=self.currency.prices["price"],
                city=self.weather.weather["city"],
                temp=self.weather.weather["temp"],
            )
        )
