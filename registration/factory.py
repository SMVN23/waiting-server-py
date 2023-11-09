# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports
from typing import Dict, Union, Tuple
from db.manager import DbManager

# Required imports
import datetime

from shared_constants import RegistrationStatus, TIMESTAMP_FORMAT, TbRegistrationsColumns
from .definition import RegistrationDefinition

class RegistrationFactory:

    def __init__(self, db_manager: DbManager) :
        self.__registration_id_generator = db_manager.get_latest_registration_id()

    def create_from_initial(self, initial_registration: Dict[str, Union[str,int]]) -> RegistrationDefinition:
        registration = RegistrationDefinition()
        registration.registration_id = self.__registration_id_generator
        registration.store_id = initial_registration[TbRegistrationsColumns.STORE_ID]
        registration.waiting_order = initial_registration[TbRegistrationsColumns.WAITING_ORDER]
        registration.phone_number = initial_registration[TbRegistrationsColumns.PHONE_NUMBER]
        registration.team_size = initial_registration[TbRegistrationsColumns.TEAM_SIZE]
        registration.timestamp = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
        registration.status = RegistrationStatus.REGISTERED

        self.__registration_id_generator += 1

        return registration

    def create_from_response(self, response_body) -> RegistrationDefinition:
        registration = RegistrationDefinition()
        for column_name, column_value in response_body.items():
            registration.set_column_value(column_name, column_value)
        return registration

    @classmethod
    def create_from_select_query(self, row: Tuple[Union[str,int]]) -> RegistrationDefinition:
        registration = RegistrationDefinition()
        registration.registration_id = row[0]
        registration.store_id = row[1]
        registration.waiting_order = row[2]
        registration.phone_number = row[3]
        registration.team_size = row[4]
        registration.timestamp = row[6]
        registration.status = row[6]
        return registration
