

from .base import HttpTestCase


class TestIndex(HttpTestCase):

    def test_idx(self):
        resp = self.fetch('/')
        self.assertEqual(resp.code, 200)

