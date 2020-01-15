
import json
from os.path import dirname, join as path_join
from unittest.mock import patch

from .base import HttpTestCase


class TestStock(HttpTestCase):

    def test_stock_no_key(self):
        # missing param
        resp = self.fetch('/sq')
        self.assertEqual(resp.code, 405)
        # missing api key
        resp = self.fetch('/sq/aapl')
        self.assertEqual(resp.code, 500)


def fake_fetch_stock(apikey, sym):
    with open(path_join(dirname(__file__),"fixtures","stock.json")) as f:
        return json.load(f)


class TestStockFetch(HttpTestCase):

    def test_stock_mocked(self):
        with patch(
                'smugapi.handlers.stockquotes._fetch_stock_data',
                fake_fetch_stock
            ):
            self.get_app().configuration.set('worldtradingdata_key', 'fake')
            resp = self.fetch('/sq/aapl')
            data = self.to_json(resp)
            self.assertEqual(resp.code, 200)
            self.assertTrue(data['text'].startswith('AAPL'))


"""
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

"""
