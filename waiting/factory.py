# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .registration import Registration
from .store import Store

class WaitingFactory:

    def __init__(self, reg_id) :
        self.__reg_id_generator = reg_id

    def create_store(self, store_id, db_manager):
        return Store(store_id, db_manager, self)

    def create_registration(self):
        registration = Registration(self.__reg_id_generator)
        self.__reg_id_generator += 1
        return registration
