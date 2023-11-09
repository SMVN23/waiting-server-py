# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Type hint imports

# Required imports
from flask import Blueprint, g, request, jsonify

bp = Blueprint("reset", __name__, url_prefix="/")

@bp.route("/reset", methods=["PUT"])
def reset_waiting_order():
    store_id = int(request.args.get("store_id"))
    g.registrations_mgr.reset_waiting_order(store_id)
    return jsonify({})
