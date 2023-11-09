
from settings import SettingsManager
from db import DbManager, DbFactory


if __name__ == "__main__":
    print("[Main] Init SettingsManager")
    setting_mgr = SettingsManager()
    setting_mgr.parse()

    print("[Main] Init WaitingFactory")
    db_factory = DbFactory()

    print("[Main] Init DatabaseManager")
    db = DbManager(db_factory)
    db.init(setting_mgr.database_server, setting_mgr.databases)
