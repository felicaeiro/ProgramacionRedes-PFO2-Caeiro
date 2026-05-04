import os
from flask import Blueprint, current_app, send_from_directory

tareas_bp = Blueprint("tareas", __name__)


@tareas_bp.route("/tareas", methods=["GET"])
def tareas():
    root_path = current_app.root_path
    return send_from_directory(root_path, "index.html")
