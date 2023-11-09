# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import Flask, g

from settings_management import SettingsManager
from waiting.db.manager import DatabaseManager
from waiting.db.waiting_factory import WaitingFactory

from registration.manager import RegistrationManager
import apis

# Init app dependencies
print("[Main] Init SettingsManager")
setting_mgr = SettingsManager()
setting_mgr.parse()

print("[Main] Init WaitingFactory")
db_factory = WaitingFactory()

print("[Main] Init DatabaseManager")
db_mgr = DatabaseManager(db_factory)
db_mgr.init(setting_mgr.database_server, setting_mgr.databases)
registrations_mgr = RegistrationManager(db_mgr)

# Init app
app = Flask(__name__)


@app.before_request
def before_first_request():
    if "registrations_mgr" not in g:
        setattr(g, "registrations_mgr", registrations_mgr)

@app.route("/")
def index():
    return "<p>Hello World!</p>"

app.register_blueprint(apis.dashboard.bp)
app.register_blueprint(apis.add.bp)
app.register_blueprint(apis.registrations.bp)
app.register_blueprint(apis.reset.bp)
app.register_blueprint(apis.status.bp)

