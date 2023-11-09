# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports
from typing import Dict

# Required imports

class Header:
    def __init__(self, order: int) -> None:
        self.order = order
        self.name = ""
        self.type = None
        self.is_primary_key = False

    def init(self, config: Dict[str, str]) -> None:
        self.name = config["NAME"]
        self.type = config["TYPE"]

    def set_primary_key(self) -> None:
        self.is_primary_key = True
