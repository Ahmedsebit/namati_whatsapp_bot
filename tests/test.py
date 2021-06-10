import io
from pathlib import Path
import unittest
import os
from flask import json, jsonify
from app.app import create_app, db


class ModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        with self.app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()
        