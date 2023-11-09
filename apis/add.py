# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports

# Required imports
from flask import Blueprint, g, request, jsonify

bp = Blueprint("add", __name__, url_prefix="/")

@bp.route("/add", methods=["POST"])
def add_registrations():
    registration = g.registrations_mgr.add_registration(request.get_json())
    return jsonify(registration.to_response())
