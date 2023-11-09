# -*- coding: utf-8 -*-

from __future__ import absolute_import

import datetime

from shared_constants import RegStatus, TIMESTAMP_FORMAT

class Registration:
    def __init__(self, reg_id):
        self.reg_id = reg_id
        self.store_id = -1
        self.waiting_order = -1
        self.phone_number = ""
        self.team_size = -1
        self.timestamp = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
        self.status = RegStatus.REGISTERED

    def fill(self, store_id, waiting_order, phone_number, team_size):
        self.store_id = store_id
        self.waiting_order = waiting_order
        self.phone_number = phone_number
        self.team_size = team_size
