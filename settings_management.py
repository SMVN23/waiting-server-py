# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports
from typing import Dict, Union

# Required imports
import os
import json

class DatabaseSetting:
    def __init__(self) -> None:
        self.host = "localhost"
        self.port = 3306
        self.username = "root"
        self.password = "root"
        self.name = "waiting"

    def parse(self, raw_settings: Dict[str, Union[str, int]]) -> None:
        self.host = raw_settings["HOST"]
        self.port = raw_settings["PORT"]
        self.username = raw_settings["USERNAME"]
        self.password = raw_settings["PASSWORD"]
        self.name = raw_settings["NAME"]

class SettingsManager:
    SETTINGS_JSON_PATH = os.path.join(os.path.dirname(__file__), "settings.json")

    def __init__(self) -> None:
        self.database = DatabaseSetting()

    def parse(self):
        with open(self.SETTINGS_JSON_PATH, "r", encoding="utf-8") as fh:
            raw_settings = json.loads(fh)
            self.database.parse(raw_settings["DATABASE"])
