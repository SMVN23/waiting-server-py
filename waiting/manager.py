# -*- coding: utf-8 -*-

from __future__ import absolute_import

from shared_constants import RegsTableHeader
from .factory import RegFactory

class RegManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.factory = RegFactory()

    def __create_store(self, store_id):
        store = RegFactory.create_store(store_id, self.db_manager)
        self.__stores[store_id] = store
        return store

    def __get_store(self, store_id):
        store = self.__stores.get(store_id)
        if store is None:
            store = self.__create_store(store_id)
        return store

    def init_store(self):
        self.__stores = {}
        for store_id in self.db_manager.get_store_ids():
            self.__create_store(store_id)

    def get_dashboard(self, store_id):
        return self.__get_store(store_id).get_dashboard()

    def add_registration(self, initial_registration):
        store_id = initial_registration[RegsTableHeader.STORE_ID]
        return self.__get_store(store_id).add_registration(initial_registration)

    def get_registrations(self, store_id):
        return self.__get_store(store_id).get_registrations()

    def reset_waiting_order(self, store_id):
        self.__get_store(store_id).reset_waiting_order()

    def change_registration_status(self, registration_json):
        store_id = registration_json[RegsTableHeader.STORE_ID]
        return self.__get_store(store_id).change_registration_status(registration_json)
