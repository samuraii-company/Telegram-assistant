import requests
from config import Config


class Weather:
    def __init__(self, city: str):
        self.weather_token = str(Config.weather_token)
        self.city = city
        self.check_data()

    def check_data(self) -> None:
        """
        Check temp data from Open weather api
        """
        req = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.weather_token}&units=metric"
        )
        self.data = req.json()

    @property
    def weather(self) -> list[str, str]:
        """
        Get temp data
        """
        return {
            "city": self.city,
            "temp": self.data["main"]["temp"]
        }
