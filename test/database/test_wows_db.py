from unittest import TestCase
from database.wows_db import Wows_database

class TestWows_database(TestCase):

    def setUp(self):
        self.wowsdb = Wows_database('test.wows.db')

    def test_getLatest(self):
        l = []
        pass

        