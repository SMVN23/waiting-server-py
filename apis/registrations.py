# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports

# Required imports
from flask import Blueprint, g, request, jsonify

bp = Blueprint("registrations", __name__, url_prefix="/")

@bp.route("/registrations", methods=["GET"])
def get_registrations():
    store_id = int(request.args.get("store_id"))
    registrations = g.registrations_mgr.get_registrations(store_id)
    return jsonify([registration.to_response() for registration in registrations.values()])
