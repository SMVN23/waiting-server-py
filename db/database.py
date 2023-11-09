# -*- coding: utf-8 -*-

from __future__ import absolute_import

class DbDatabase:
    def __init__(self, factory):
        self.factory = factory
        self.name = ""
        self.client = self.factory.create_client()
        self.tables = {}

    def init(self, server_setting, database_setting):
        self.client.connect(server_setting, database_setting.name)

        self.name = database_setting.name
        for table_setting in database_setting.tables:
            table = self.factory.create_table(self.client)
            table.init(table_setting)
            table.create()
            self.tables[table.name] = table


