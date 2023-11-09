# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports

# Required imports
from flask import Blueprint, g, request, jsonify
from shared_constants import TOTAL_REGISTRATIONS, TOTAL_WAITING_MINUTES, WAITING_MINUTES_PER_TEAM

bp = Blueprint("status", __name__, url_prefix="/")

@bp.route("/status", methods=["PUT"])
def change_registration_status():
    total_registrations, waiting_minutes_per_team = g.registrations_mgr.change_registration_status(request.get_json())
    return jsonify({
        TOTAL_REGISTRATIONS: total_registrations,
        TOTAL_WAITING_MINUTES: total_registrations*waiting_minutes_per_team,
        WAITING_MINUTES_PER_TEAM: waiting_minutes_per_team
    })
