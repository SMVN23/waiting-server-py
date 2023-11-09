# -*- coding: utf-8 -*-

from __future__ import absolute_import

class DbManager:
    def __init__(self, factory) -> None:
        self.factory = factory
        self.databases = {}

    def init(self, server_setting, database_settings) -> None:
        for database_setting in database_settings:
            database = self.factory.create_database()
            database.init(server_setting, database_setting)
            self.databases[database.name] = database

    # def create_tb_registrations_if_not_exist(self):
    #     query = f"CREATE TABLE IF NOT EXISTS {TB_REGISTRATIONS_NAME} (" \
    #             f"{TbRegistrationsColumns.REGISTRATION_ID} INTEGER PRIMARY KEY, " \
    #             f"{TbRegistrationsColumns.STORE_ID} INTEGER, " \
    #             f"{TbRegistrationsColumns.WAITING_ORDER} INTEGER, " \
    #             f"{TbRegistrationsColumns.PHONE_NUMBER} TEXT, " \
    #             f"{TbRegistrationsColumns.TEAM_SIZE} INTEGER, " \
    #             f"{TbRegistrationsColumns.TIMESTAMP} TEXT, " \
    #             f"{TbRegistrationsColumns.STATUS} INTEGER " \
    #             ")"
    #     self.__mariadb_client.exec_query(query)

    # def add_registration(self, query):
    #     self.__mariadb_client.exec_query(query)

    # def get_latest_registration_id(self) -> int:
    #     query = f"SELECT {TbRegistrationsColumns.REGISTRATION_ID} FROM {TB_REGISTRATIONS_NAME} " \
    #             f"ORDER BY {TbRegistrationsColumns.REGISTRATION_ID} DESC LIMIT 1"
    #     rows = self.__mariadb_client.exec_select_query(query)
    #     latest_registration_id = 0
    #     if rows and rows[0]:
    #         latest_registration_id = rows[0][0]
    #     return latest_registration_id + 1

    # def get_latest_waiting_order(self, store_id: int) -> int:
    #     query = f"SELECT {TbRegistrationsColumns.REGISTRATION_ID}, {TbRegistrationsColumns.WAITING_ORDER} " \
    #             f"FROM {TB_REGISTRATIONS_NAME} WHERE {TbRegistrationsColumns.STORE_ID}='{store_id}' " \
    #             f"ORDER BY {TbRegistrationsColumns.REGISTRATION_ID} DESC LIMIT 1"
    #     rows = self.__mariadb_client.exec_select_query(query)
    #     latest_waiting_order = 0
    #     if rows and rows[0]:
    #         latest_waiting_order = rows[0][1]
    #     return latest_waiting_order + 1

    # def get_store_ids(self) -> List[int]:
    #     query = f"SELECT {TbRegistrationsColumns.STORE_ID} FROM {TB_REGISTRATIONS_NAME} GROUP BY " \
    #             f"{TbRegistrationsColumns.STORE_ID}"
    #     rows = self.__mariadb_client.exec_select_query(query)
    #     store_ids = []
    #     for row in rows:
    #         store_ids.append(row[0])
    #     return store_ids

    # def get_registrations(self, store_id, status=None) -> Tuple[Tuple[Union[str,int]]]:
    #     column_names_str = ", ".join(TB_REGISTRATIONS_ALL_COLUMNS)
    #     query = f"SELECT {column_names_str} FROM {TB_REGISTRATIONS_NAME} " \
    #             f"WHERE {TbRegistrationsColumns.STORE_ID}='{store_id}'"
    #     if status is not None:
    #         query += f" AND {TbRegistrationsColumns.STATUS}='{status}'"
    #     return self.__mariadb_client.exec_select_query(query)

    # def change_registration_status(self, registration_id, status):
    #     query = f"UPDATE {TB_REGISTRATIONS_NAME} " \
    #             f"SET {TbRegistrationsColumns.STATUS}='{status}' " \
    #             f"WHERE {TbRegistrationsColumns.REGISTRATION_ID}='{registration_id}'"

    #     self.__mariadb_client.exec_query(query)

