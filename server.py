# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports

# Required imports
from flask import Flask, g

from db.mariadb_client import MariaDbClient
from db.manager import DbManager
from registration.manager import RegistrationManager
import apis

# Init app dependencies
mariadb_client = MariaDbClient()
db_mgr = DbManager(mariadb_client)
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

