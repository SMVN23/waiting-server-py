# -*- coding: utf-8 -*-

from __future__ import absolute_import


class DbTable:
    def __init__(self, factory, client):
        self.factory = factory
        self.name = ""
        self.client = client
        self.headers = {}

    def init(self, setting):
        self.name = setting.name
        for header_name, header_type in setting.headers.items():
            header = self.factory.create_header(header_name, header_type)
            self.headers[header.name] = header
        self.headers[setting.primary_key].set_primary_key()

    def remove(self):
        query = f"DROP TABLE IF EXISTS {self.name}"
        self.client.exec_query_and_commit(query)

    def create(self, replace=False):
        if replace:
            query = f"DROP TABLE IF EXISTS {self.name}"
            self.client.exec_query(query)

        headers_query = []
        for header in self.headers.values():
            if header.is_primary_key:
                headers_query.append(f"{header.name} {header.type} PRIMARY KEY")
            else:
                headers_query.append(f"{header.name} {header.type}")

        query = f"CREATE TABLE IF NOT EXISTS {self.name} ({','.join(headers_query)})"
        self.client.exec_query_and_commit(query)

    def add_row(self, header_values):
        if len(header_values) != len(self.headers):
            print(f"ERROR: [{self.name}] Cannot add row because of missing data")
        else:
            header_values_str = "','".join([str(value) for value in header_values])
            header_names_str = ",".join(list(self.headers.keys()))
            query = f"INSERT INTO {self.name} ({header_names_str}) VALUES ('{header_values_str}')"
            self.client.exec_query_and_commit(query)

    def get_rows(self, header_names, conditions):
        header_names_str = ",".join(header_names)

        condition_strlist = []
        for header_name, header_value in conditions.items():
            condition_strlist.append(f"{header_name}='{header_value}'")
        condition_str = " AND ".join(condition_strlist)

        query = f"SELECT {header_names_str} FROM {self.name} WHERE {condition_str}"
        raw_rows = self.client.exec_query(query)

        rows = []
        for raw_row in raw_rows:
            for i, header_name in enumerate(header_names):
                rows.append({header_name: raw_row[i]})
        return rows

    def update_columns(self, rows, conditions):
        header_query_strlist = []
        for header_name, header_value in rows.items():
            header_query_strlist.append(f"{header_name}='{header_value}'")
        header_query_str = ",".join(header_query_strlist)

        condition_strlist = []
        for header_name, header_value in conditions.items():
            condition_strlist.append(f"{header_name}='{header_value}'")
        condition_str = " AND ".join(condition_strlist)

        query = f"UPDATE {self.name} SET {header_query_str} WHERE {condition_str}"
        self.client.exec_query_and_commit(query)
