
import json
from os.path import dirname, join as path_join
from unittest.mock import patch

from .base import HttpTestCase


class TestWeather(HttpTestCase):

    def test_weather_no_api(self):
        # missing param
        resp = self.fetch('/weather')
        self.assertEqual(resp.code, 400)
        # missing api key
        resp = self.fetch('/weather?city=austin+tx')
        self.assertEqual(resp.code, 500)


def fake_fetch_weather(apikey, wtype, loc, country="US"):
    with open(path_join(dirname(__file__),"fixtures","weather.json")) as f:
        return json.load(f)


def fake_fetch_forecast(apikey, wtype, loc, country="US"):
    with open(path_join(dirname(__file__),"fixtures","forecast.json")) as f:
        return json.load(f)


class TestMockedWeather(HttpTestCase):
    def test_weather_mocked(self):
        with patch(
                'smugapi.handlers.weatherbit._fetch_weather',
                fake_fetch_weather
                ):
            self.get_app().configuration.set('weatherbit_apikey', 'fake')
            # app._weatherbit_apikey = 'fake'
            resp = self.fetch('/weather?city=austin,tx')
            data = self.to_json(resp)
            print(data)
            self.assertEqual(data['ok'], True)
            self.assertTrue(data['text'].startswith('weather for Cedar Park'))

    def test_forecast_mocked(self):
        with patch(
                'smugapi.handlers.weatherbit._fetch_forecast',
                fake_fetch_forecast
                ):
            self.get_app().configuration.set('weatherbit_apikey', 'fake')
            resp = self.fetch('/forecast?city=austin,tx')
            data = self.to_json(resp)
            print(data)
            self.assertEqual(data['ok'], True)
            self.assertTrue(data['text'].startswith('forecast for Will'))


