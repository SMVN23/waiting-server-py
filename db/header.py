# -*- coding: utf-8 -*-

from __future__ import absolute_import

class DbHeader:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.is_primary_key = False

    def set_primary_key(self):
        self.is_primary_key = True
