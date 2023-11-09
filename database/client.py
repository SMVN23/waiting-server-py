# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports
from typing import Tuple, Any
from settings_management import DatabaseSetting

# Required imports
import sys
import pymysql

class DbClient:

    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self, setting: DatabaseSetting):
        try:
            self.__connection = pymysql.connect(
                host=setting.host,
                port=setting.port,
                user=setting.username,
                password=setting.password,
                database=setting.name
            )
            self.__cursor = self.__connection.cursor()
        except pymysql.Error as e:
            print(f"Error connecting to Database http://{setting.username}:****@{setting.host}:{setting.port}/{setting.name}: {e}")
            sys.exit(-1)

    def disconnect(self):
        if self.__connection is not None:
            self.__connection.close()

    def exec_query(self, query: str) -> Tuple[Tuple[Any]]:
        try:
            self.__cursor.execute(query)
            print(f"Success to execute query: {query}")

            rows = []
            for row in self.__cursor:
                rows.append(row)
            return rows
        except pymysql.Error as e:
            print(f"Error execute query: {query}\n    {e}")

    def exec_query_and_commit(self, query: str) -> Tuple[Tuple[Any]]:
        rows = self.exec_query(query)
        self.__connection.commit()
        return rows
