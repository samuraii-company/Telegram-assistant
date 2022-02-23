from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()


@dataclass
class Config:
    """
    Congigurations class
    """
    token: str = os.getenv("token")
    admin_id: int = os.getenv("admin_id")
    api_key: str = os.getenv("api_key")
    api_secret: str = os.getenv("api_secret")
    weather_token: str = os.getenv("weather_token")


wake_up_message = """\
Доброе утро сэр,

Цены на криптовалюты
BTC: {btc}
EHT: {eth}
ADA: {ada}
XRP: {xrp}

Доллар: сейчас равен {usd}

Погода в гододе {city} состовляет {temp} C

Приятного дня
    """
