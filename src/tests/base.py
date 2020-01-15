
import json
from unittest import TestCase

from tornado.testing import AsyncHTTPTestCase

from smugapi.main import make_app


class HttpTestCase(AsyncHTTPTestCase):
    def get_app(self):
        if not hasattr(self, '_app'):
            self._app = make_app()
        return self._app

    def to_json(self, resp):
        return json.loads(resp.body)

