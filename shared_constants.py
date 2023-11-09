# -*- coding: utf-8 -*-

from __future__ import absolute_import

DB_NAME = "waiting"

TB_REGISTRATIONS_NAME = "tb_registrations"

class RegistrationStatus:
    UNDEFINED = -1
    REGISTERED = 0
    ENTERED = 1
    CANCELLED = 2
    NOT_ENTERED = 3


class TbRegistrationsColumns:
    REGISTRATION_ID = "REGISTRATION_ID"
    STORE_ID = "STORE_ID"
    WAITING_ORDER = "WAITING_ORDER"
    PHONE_NUMBER = "PHONE_NUMBER"
    TEAM_SIZE = "TEAM_SIZE"
    TIMESTAMP = "TIMESTAMP"
    STATUS = "STATUS"

TB_REGISTRATIONS_ALL_COLUMNS = [
    TbRegistrationsColumns.REGISTRATION_ID,
    TbRegistrationsColumns.STORE_ID,
    TbRegistrationsColumns.WAITING_ORDER,
    TbRegistrationsColumns.PHONE_NUMBER,
    TbRegistrationsColumns.TEAM_SIZE,
    TbRegistrationsColumns.TIMESTAMP,
    TbRegistrationsColumns.STATUS
]

TOTAL_REGISTRATIONS = "TOTAL_REGISTRATIONS"
TOTAL_WAITING_MINUTES = "TOTAL_WAITING_MINUTES"
WAITING_MINUTES_PER_TEAM = "WAITING_MINUTES_PER_TEAM";

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
