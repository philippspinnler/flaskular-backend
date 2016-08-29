import unittest
import json
from flaskular import app
from flask import current_app


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @staticmethod
    def parseJsonResponse(rv):
        return json.loads(rv.data)
