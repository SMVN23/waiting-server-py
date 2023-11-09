# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports
from typing import Dict, Union

# Required imports
from shared_constants import TB_REGISTRATIONS_NAME, TbRegistrationsColumns, \
    TB_REGISTRATIONS_ALL_COLUMNS, RegistrationStatus

class RegistrationDefinition:
    def __init__(self):
        self.registration_id = -1
        self.store_id = -1
        self.waiting_order = -1
        self.phone_number = ""
        self.team_size = -1
        self.timestamp = "yyyy-mm-dd HH:MM:SS"
        self.status = RegistrationStatus.UNDEFINED

    def get_column_value(self, column_name: str) -> Union[str, int]:
        if column_name == TbRegistrationsColumns.REGISTRATION_ID:
            return self.registration_id
        elif column_name == TbRegistrationsColumns.STORE_ID:
            return self.store_id
        elif column_name == TbRegistrationsColumns.WAITING_ORDER:
            return self.waiting_order
        elif column_name == TbRegistrationsColumns.PHONE_NUMBER:
            return self.phone_number
        elif column_name == TbRegistrationsColumns.TEAM_SIZE:
            return self.team_size
        elif column_name == TbRegistrationsColumns.TIMESTAMP:
            return self.timestamp
        elif column_name == TbRegistrationsColumns.STATUS:
            return self.status
        else:
            raise ValueError(f"Unknown column name {column_name}")

    def set_column_value(self, column_name: str, column_value: Union[str, int]) -> None:
        if column_name == TbRegistrationsColumns.REGISTRATION_ID:
            self.registration_id = column_value
        elif column_name == TbRegistrationsColumns.STORE_ID:
            self.store_id = column_value
        elif column_name == TbRegistrationsColumns.WAITING_ORDER:
            self.waiting_order = column_value
        elif column_name == TbRegistrationsColumns.PHONE_NUMBER:
            self.phone_number = column_value
        elif column_name == TbRegistrationsColumns.TEAM_SIZE:
            self.team_size = column_value
        elif column_name == TbRegistrationsColumns.TIMESTAMP:
            self.timestamp = column_value
        elif column_name == TbRegistrationsColumns.STATUS:
            self.status = column_value
        else:
            raise ValueError(f"Unknown column name {column_name}")

    def to_response(self) -> Dict[str, Union[str,int]]:
        response_body = {}
        for column_name in TB_REGISTRATIONS_ALL_COLUMNS:
            response_body[column_name] = self.get_column_value(column_name)
        return response_body

    def to_insert_query(self) -> str:
        column_values = []
        for column_name in TB_REGISTRATIONS_ALL_COLUMNS:
            column_values.append(str(self.get_column_value(column_name)))
        column_values_str = "', '".join(column_values)

        column_names_str = ", ".join(TB_REGISTRATIONS_ALL_COLUMNS)
        return f"INSERT INTO {TB_REGISTRATIONS_NAME} ({column_names_str}) VALUES ('{column_values_str}')"

