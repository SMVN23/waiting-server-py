# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports
from typing import Dict, Union
from db.manager import DbManager

# Required imports
from shared_constants import TbRegistrationsColumns
from .factory import RegistrationFactory
from .store import RegistrationStore

class RegistrationManager:
    def __init__(self, db_manager: DbManager) -> None:
        self.__db_manager = db_manager
        self.__factory = RegistrationFactory(self.__db_manager)
        self.__stores = {}
        for store_id in self.__db_manager.get_store_ids():
            self.__create_store(store_id)

    def __create_store(self, store_id: int) -> RegistrationStore:
        store = RegistrationStore(store_id, self.__db_manager, self.__factory)
        self.__stores[store_id] = store
        return store

    def __get_store(self, store_id: int) -> RegistrationStore:
        store = self.__stores.get(store_id)
        if store is None:
            store = self.__create_store(store_id)
        return store

    def get_dashboard(self, store_id: int):
        return self.__get_store(store_id).get_dashboard()

    def add_registration(self, initial_registration):
        store_id = initial_registration[TbRegistrationsColumns.STORE_ID]
        return self.__get_store(store_id).add_registration(initial_registration)

    def get_registrations(self, store_id: int):
        return self.__get_store(store_id).get_registrations()

    def reset_waiting_order(self, store_id: int):
        self.__get_store(store_id).reset_waiting_order()

    def change_registration_status(self, registration_json: Dict[str, Union[int, str]]):
        store_id = registration_json[TbRegistrationsColumns.STORE_ID]
        return self.__get_store(store_id).change_registration_status(registration_json)
