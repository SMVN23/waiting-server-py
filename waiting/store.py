# -*- coding: utf-8 -*-

from __future__ import absolute_import

from shared_constants import RegStatus, INITIAL_WAITING_ORDER, INITIAL_WAITING_TIME_PER_TEAM

class WaitingStore:
    def __init__(self, store_id, db_adapter):
        self.__store_id = store_id
        self.__db_adapter = db_adapter

        self.__waiting_order = INITIAL_WAITING_ORDER
        self.__waiting_minutes_per_team = INITIAL_WAITING_TIME_PER_TEAM
        self.__registrations = {}

    def init_registrations(self):
        registrations = self.__db_adapter.get_registrations(self.__store_id, RegStatus.REGISTERED)
        for registration in registrations:
            self.__registrations[registration.get_id()] = registration

        self.__waiting_order = self.__db_adapter.get_last_waiting_order(self.__store_id)
        self.__waiting_minutes_per_team = self.__db_adapter.get_waiting_minutes_per_team(self.__store_id)

    def get_registrations(self):
        return self.__registrations

    def get_dashboard(self):
        return (len(list(self.__registrations.keys())), self.__waiting_minutes_per_team)

    def add_registration(self, registration):
        registration.fill_store_info(self.__store_id, self.__waiting_order)
        self.__registrations[registration.get_id()] = registration
        self.__db_adapter.add_registration(registration)
        self.__waiting_order += 1
        return registration

    def reset_waiting_order(self):
        self.__waiting_order = INITIAL_WAITING_ORDER

    def change_registration_status(self, reg_id, reg_status):
        self.__db_adapter.change_registration_status(reg_id, reg_status)
        del self.__registrations[reg_id]
        return self.get_dashboard()
