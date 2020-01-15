
from os import environ
from unittest import TestCase

from smugapi.main import Configuration


class TestConfiguration(TestCase):

    def test_config_val(self):
        cfg = Configuration(feh="blarg")
        self.assertEqual("blarg", cfg('feh'))

    def test_config_env(self):
        cfg = Configuration()
        self.assertEqual(None, cfg('meh'))

        environ['SMUG_MEH'] = 'blipper'
        self.assertEqual('blipper', cfg('meh'))


