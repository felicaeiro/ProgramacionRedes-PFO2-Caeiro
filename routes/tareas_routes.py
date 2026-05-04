from flask import Blueprint, render_template

tareas_bp = Blueprint("tareas", __name__)


@tareas_bp.route("/tareas", methods=["GET"])
def tareas():
    return render_template("tareas.html")
