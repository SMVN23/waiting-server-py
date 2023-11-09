# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports
from typing import Dict, Tuple, Union
from db.manager import DbManager
from .factory import RegistrationFactory
from .definition import RegistrationDefinition

# Required imports
from shared_constants import RegistrationStatus, TbRegistrationsColumns

class RegistrationStore:
    def __init__(self, store_id: int, db_manager: DbManager, factory: RegistrationFactory):
        self.__store_id = store_id
        self.__db_manager = db_manager
        self.__factory = factory
        self.__registrations = {}
        for row in self.__db_manager.get_registrations(self.__store_id, RegistrationStatus.REGISTERED):
            registration = self.__factory.create_from_select_query(row)
            self.__registrations[registration.registration_id] = registration

        self.__waiting_order = self.__db_manager.get_latest_waiting_order(self.__store_id)
        self.__waiting_minutes_per_team = 10

    def get_store_id(self) -> int:
        return self.__store_id

    def get_registrations(self) -> Dict[int, RegistrationDefinition]:
        return self.__registrations

    def get_dashboard(self) -> Tuple[int, int]:
        return (len(list(self.__registrations.keys())), self.__waiting_minutes_per_team)

    def add_registration(self, initial_registration: Dict[str, Union[str,int]]) -> RegistrationDefinition:
        initial_registration[TbRegistrationsColumns.WAITING_ORDER] = self.__waiting_order
        registration = self.__factory.create_from_initial(initial_registration)
        self.__registrations[registration.registration_id] = registration
        self.__db_manager.add_registration(registration.to_insert_query())
        self.__waiting_order += 1
        return registration

    def reset_waiting_order(self) -> None:
        self.__waiting_order = 1

    def change_registration_status(self, registration_json: Dict[str, Union[int, str]]):
        registration_id = registration_json[TbRegistrationsColumns.REGISTRATION_ID]
        status = registration_json[TbRegistrationsColumns.STATUS]
        del self.__registrations[registration_id]
        self.__db_manager.change_registration_status(registration_id, status)
        return self.get_dashboard()
