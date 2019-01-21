import unittest
from run import app

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client(self)